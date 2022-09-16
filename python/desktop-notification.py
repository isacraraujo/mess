#pip install win10toast
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast(
    "Notificação",
    "Eaeeee",
    threaded=True,
    icon_path=None,
    duration=3
)