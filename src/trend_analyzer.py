import numpy as np

history = []
last_alert = None

def update_history(score, max_len=20):
    history.append(score)
    if len(history) > max_len:
        history.pop(0)

def analyze_trend():
    if len(history) < 5:
        return None, None

    x = np.arange(len(history))
    slope = np.polyfit(x, history, 1)[0]
    future_score = history[-1] + slope * 5

    return slope, future_score

def get_alert():
    global last_alert

    slope, future = analyze_trend()

    if slope is None:
        return None

    alert = None

    if slope < -2:
        alert = "⚠️ Health dropping rapidly"

    elif future is not None and future < 40:
        alert = "🚨 System may become CRITICAL soon"

    # avoid repeated popup spam
    if alert == last_alert:
        return None

    last_alert = alert
    return alert