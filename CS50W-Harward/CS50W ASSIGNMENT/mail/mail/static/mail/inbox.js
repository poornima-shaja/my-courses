document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', (event) => {
    event.preventDefault(); // Stop page reload

    // Read values from form
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    // Send email via POST
    fetch('/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
      })
    })
    .then(response => response.json())
    .then(result => {
      console.log(result); 
      load_mailbox('sent'); 
    });
  });

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  

}

function load_mailbox(mailbox) {
  const emails_view = document.querySelector('#emails-view');
  const compose_view = document.querySelector('#compose-view');

  // Show mailbox, hide compose
  emails_view.style.display = 'block';
  compose_view.style.display = 'none';

  // Clear previous content and show mailbox name
  emails_view.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch emails for this mailbox
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      emails.forEach(email => {
        const email_div = document.createElement('div');

        // Show sender/subject/timestamp
        email_div.innerHTML = `
          <strong>From:</strong> ${email.sender} 
          <strong>Subject:</strong> ${email.subject} 
          <span style="float:right">${email.timestamp}</span>
        `;

        // Styling
        email_div.style.border = '1px solid black';
        email_div.style.padding = '10px';
        email_div.style.margin = '5px 0';
        email_div.style.cursor = 'pointer';
        email_div.style.backgroundColor = email.read ? 'lightgray' : 'white';

        // Click to view email
        email_div.addEventListener('click', () => view_email(email.id));

        // Append to mailbox view
        emails_view.append(email_div);
      });
    });
}


function view_email(email_id) {
  const emails_view = document.querySelector('#emails-view');
  const compose_view = document.querySelector('#compose-view');

  // Hide compose view
  compose_view.style.display = 'none';

  // Fetch the email details
  fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email => {
      // Mark email as read
      fetch(`/emails/${email_id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({read: true})
      });

      // Display email details
      emails_view.innerHTML = `
        <p><strong>From:</strong> ${email.sender}</p>
        <p><strong>To:</strong> ${email.recipients.join(', ')}</p>
        <p><strong>Subject:</strong> ${email.subject}</p>
        <p><strong>Timestamp:</strong> ${email.timestamp}</p>
        <hr>
        <p style="white-space: pre-line;">
  ${email.body.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}
</p>

      `;

      // Add Archive/Unarchive button only if this is not a sent email
if (email.sender !== document.querySelector('h2').innerText) {
    const archive_button = document.createElement('button');
    archive_button.className = 'btn btn-sm btn-outline-primary';
    archive_button.innerText = email.archived ? 'Unarchive' : 'Archive';

    // Attach click event
    archive_button.addEventListener('click', () => {
        fetch(`/emails/${email.id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                archived: !email.archived
            })
        })
        .then(() => {
            load_mailbox('inbox'); // reload inbox after archiving/unarchiving
        });
    });

    emails_view.appendChild(archive_button);
}

// Add Reply button
const reply_button = document.createElement('button');
reply_button.className = 'btn btn-sm btn-outline-primary';
reply_button.innerText = 'Reply';

// Click event for Reply
reply_button.addEventListener('click', () => {
    compose_email(); // show the compose form

    // Pre-fill fields
    document.querySelector('#compose-recipients').value = email.sender;

    // Pre-fill subject with "Re: " if not already
    if (email.subject.startsWith("Re: ")) {
        document.querySelector('#compose-subject').value = email.subject;
    } else {
        document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
    }

    document.querySelector('#compose-body').value =
`\n\nOn ${email.timestamp}, ${email.sender} wrote:\n> ${email.body.replace(/\n/g, '\n> ')}`;


});

// Append Reply button
emails_view.appendChild(reply_button);


      // Show the emails-view
      emails_view.style.display = 'block';
    });
}