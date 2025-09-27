# SMTP Client Lab (Updated Version with STARTTLS)

This lab demonstrates sending an email using Python sockets and the Gmail SMTP server with STARTTLS security.

## Steps to Run

1. Enable **2-Step Verification** on your Gmail account.
2. Generate an **App Password** from your Google Account Security settings.
3. Update the `sender`, `password`, and `recipient` fields in `SMTPClient.py`.
4. Run the script:

```bash
python SMTPClient.py
```

## Expected Output

You should see the SMTP command/response flow, ending with:

```
✅ Email sent successfully!
```

If you encounter `530 Must issue a STARTTLS command first`, this updated script fixes it by initiating a secure TLS session.