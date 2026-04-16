from src.collector import collect_metrics
from src.feature_engineering import process_features
from src.health_engine import predict_health
from src.trend_analyzer import update_history, get_alert

def get_system_health():
    # 1. Collect metrics
    metrics = collect_metrics()

    # 2. Feature engineering
    features = process_features(metrics)

    # 3. Predict
    score, category = predict_health(features)

    # 4. Trend tracking
    update_history(score)
    alert = get_alert()

    # 5. Return structured output
    return {
        "score": int(score),
        "category": category,
        "alert": alert   # None or message
    }