import nltk

nltk.data.path.append('/opt/render/nltk_data')
nltk.download('vader_lexicon')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *
import string
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Register
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "processor/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "processor/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "processor/register.html")

# login
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "processor/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "processor/login.html")

# logout
def logout_view(request):
    logout(request)
    return redirect("index")

# index
def index(request):
    if request.user.is_authenticated:
        all_analyze_text = Analyze.objects.filter(user=request.user).order_by("-timestamp")
        sentiment_count = Analyze.objects.filter(user=request.user, tool_type="Sentiment Analysis").count()
        summary_count = Analyze.objects.filter(user=request.user, tool_type="Summarization").count()
        extract_keyword_count = Analyze.objects.filter(user=request.user, tool_type="Extract Keyword").count()
        total_count = Analyze.objects.filter(user=request.user).count()
    else:
        all_analyze_text = []
        total_count = 0
        sentiment_count = 0
        summary_count = 0
        extract_keyword_count = 0 
        
    return render(request, "processor/index.html",{
        "all_analyze_text":all_analyze_text,
        "sentiment_count":sentiment_count,
        "summary_count":summary_count,
        "extract_keyword_count": extract_keyword_count,
        "total_count":total_count
    })

# analyze sentiment
def analyze(request):
    if request.method == "POST":
        analyze_text = request.POST["analyze_text"]
        text_lowercase = analyze_text.lower()
        cleaned_text = text_lowercase.translate(str.maketrans('','',string.punctuation))
        tokenized_words = cleaned_text.split()
        word_count = len(tokenized_words)

        try:
            sid = SentimentIntensityAnalyzer()
        except:
            import nltk
            nltk.download('vader_lexicon')
            sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(analyze_text)
        compound_score = scores['compound']
        if compound_score >= 0.05:
            sentiment_label = "Positive"
        elif compound_score <= -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        Analyze.objects.create(user=request.user, analyze_text=analyze_text, tool_type="Sentiment Analysis", sentiment_score=compound_score,
            sentiment_label=sentiment_label,
            word_count=word_count, pos_score=scores['pos'],
            neg_score=scores['neg'],
            neu_score=scores['neu'])
        return JsonResponse({
            "score": scores['compound'],
            "pos": scores['pos'],
            "neg": scores['neg'],
            "neu": scores['neu'],
            "labels": sentiment_label
           
        })
    return render(request, "processor/analyze.html")

# detail
def details(request, result_id):
    result = get_object_or_404(Analyze, id=result_id, user=request.user)
    keywords = []
    if result.tool_type == "Extract Keyword" and result.keyword_text:
        keywords = [k.strip() for k in result.keyword_text.split(",")]
    return render(request, "processor/details.html",{
        "result":result,
        "keywords": keywords
    })

# delete
def delete(request, id):
    if request.method == "POST":
        item = get_object_or_404(Analyze, id=id, user=request.user)
        item.delete()
    return redirect('index')

# summary
def summarize(request):
    summary_text = ""
    original_text = ""

    if request.method == "POST":
        original_text = request.POST.get("summarize_text", "").strip()

        if original_text:
            sentences = original_text.split(". ")
            words = original_text.lower().translate(str.maketrans('', '', string.punctuation)).split()

            word_freq = Counter(words)

            sentence_scores = {}
            for sentence in sentences:
                for word in sentence.lower().split():
                    if word in word_freq:
                        sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]
            top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
            top_sentences = sorted(top_sentences, key=lambda s: sentences.index(s))
            summary_text = ". ".join(top_sentences).strip() + "."

            obj = Analyze.objects.create(
                user=request.user,
                analyze_text=original_text,
                tool_type="Summarization",
                summary_text=summary_text
            )

            return JsonResponse({
                "summary": summary_text,
                'id': obj.id
            })

    return render(request, "processor/summarize.html", {
        "original": original_text
    })

def extract_keyword(request):
    if request.method == "POST":
        keyword_text = request.POST.get("keyword_text", "")

        try:
            import string
            from collections import Counter

            # Clean text
            words = keyword_text.lower().translate(
                str.maketrans('', '', string.punctuation)
            ).split()

            # Remove common stopwords manually
            stopwords = {
                "the","is","and","in","to","of","a","for","on","with",
                "as","by","an","at","from","that","this","it"
            }

            filtered_words = [w for w in words if w not in stopwords]

            # Count frequency
            word_freq = Counter(filtered_words)

            # Get top 10 keywords
            keywords = [word for word, _ in word_freq.most_common(10)]

        except Exception as e:
            print("KEYWORD ERROR:", e)
            keywords = ["Keyword extraction failed"]

        obj = Analyze.objects.create(
            user=request.user,
            tool_type="Extract Keyword",
            analyze_text=keyword_text,
            word_count=len(keyword_text.split()),
            keyword_text=", ".join(keywords)
        )

        return JsonResponse({
            "keywords": keywords,
            "id": obj.id
        })

    return render(request, "processor/extract_keyword.html")