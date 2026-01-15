from django.shortcuts import render, redirect
from . import util
import markdown2  
import random
from django import forms

# Display All the entries
def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

# Display the markdown to html page of respective entires
def entry(request, title):
    content = util.get_entry(title)
    if content is not None:
        html_content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html",{
        "title": title,
        "html_content":html_content
    })
    else:
        return render(request, "encyclopedia/entry.html",{
        "error": "The page you're looking for does not exist!"
        })

#To search any entires from the list and even if its substring
def search(request):
    query = request.GET.get("q").strip()
    entries = util.list_entries()

    for entry in entries:
        if entry.lower() == query.lower():
            return redirect('entry' , title = entry)

    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html",{
        "query":query ,
        "results":matching_entries
    })

#To display and random page of Entries
def random_page(request):
    entries = util.list_entries()
    random_entries = random.choice(entries)
    return redirect('entry', title=random_entries)

#Form for New Entry and Content
class NewForm(forms.Form):
    title= forms.CharField(label="New title")
    content= forms.CharField(
           widget=forms.Textarea,
           label="Enter your content here:"
       )    

#Storing and Displaying New Content and if already presnet show error
def new(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title):
                return render(request, "encyclopedia/new_page.html",{
                    "form":form,
                    "error": "An entry with this title already exists!"
                } )
            util.save_entry(title, content)
            return redirect('entry', title=title)
    else:
        form = NewForm()
    return render(request, "encyclopedia/new_page.html",{
        "form":form,
        })

#form for Edit the content 
class EditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Edit")

#Edit the content and save it on the same entries
def edit(request, title):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
        util.save_entry(title, content)
        return redirect('entry', title=title)
    else:
        content = util.get_entry(title)
        if content is None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page doesn't exist to edit."
            })
        form=EditForm(initial={
            "content": content
            })

        return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": title
    })