from django.core.mail import send_mail


def send_otp(mail, otp):
    try:
        send_mail(
            subject="Delivery: sizga birmartalik tasdiqlash kodini yubordik",
            message=f"Sizning tasdiqlash kodinggiz: {otp}",
            from_email='sharofidinovjamshid@gmail.com',
            recipient_list=[mail],
            fail_silently=False
        )
        return True
    except:
        return False
