def analyze_response(user_answer, ideal_answer):
    """Evaluates user answer against the ideal answer."""
    user_answer = user_answer.lower()
    ideal_answer = ideal_answer.lower()
    
    if user_answer in ideal_answer:
        return "✅ Correct", 1.0
    elif any(word in ideal_answer for word in user_answer.split()):
        return "⚠️ Partially Correct", 0.5
    else:
        return "❌ Incorrect", 0.0




