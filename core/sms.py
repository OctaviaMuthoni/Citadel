import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='ad0ec59f8a9b543c5d93161f203470ce55365108fc2aa9c22dab6421febe1095'
)

sms = africastalking.SMS


def sending():
    # Set the numbers in international format
    recipients = ["+254718758807"]
    # Set your message
    message = "Hey AT Ninja!";
    # Set your shortCode or senderId
    sender = "22509"
    try:
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f'Houston, we have a problem: {e}')

sending()