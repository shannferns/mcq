import streamlit as st

def display_quiz(questions):
    user_answers = []
    for i, question_data in enumerate(questions):
        st.write(f"Q{i + 1}: {question_data['question']}")
        user_answer = st.radio(f"Select an answer for Q{i + 1}:", question_data['options'])
        user_answers.append(user_answer)
    return user_answers

def calculate_score(user_answers, questions):
    score = 0
    for user_answer, question_data in zip(user_answers, questions):
        if user_answer == question_data['answer']:
            score += 1
    return score

def main():
    st.set_page_config(page_title="MPhil Mock Tests", page_icon="🧠", layout="wide", initial_sidebar_state="collapsed")
    st.title("MPhil Mock Tests")

    # Define collapsible sections for different topics
    with st.expander("Motivation Theories"):
        motivation_questions = [
            {
                'question': "What is the need hierarchy theory proposed by Abraham Maslow?",
                'options': ["Physiological, Safety, Social, Esteem, Self-actualization", "Social, Esteem, Self-actualization, Physiological, Safety", "Self-actualization, Esteem, Social, Safety, Physiological", "Safety, Physiological, Esteem, Self-actualization, Social"],
                'answer': "Physiological, Safety, Social, Esteem, Self-actualization"
            },
    {
        'question': "According to Herzberg's Two-Factor Theory, which of the following is considered a hygiene factor?",
        'options': ["Achievement", "Salary", "Recognition", "Growth"],
        'answer': "Salary"
    },
    {
        'question': "Which motivation theory emphasizes the importance of self-efficacy in driving behavior?",
        'options': ["Equity Theory", "Expectancy Theory", "Hierarchy of Needs", "Self-Determination Theory"],
        'answer': "Expectancy Theory"
    },
    {
        'question': "What does the term 'ERG' represent in the context of motivation theories?",
        'options': ["Enduring, Relevant, Goals", "Existence, Relatedness, Growth", "Expectancy, Reinforcement, Goal", "Efficiency, Recognition, Growth"],
        'answer': "Existence, Relatedness, Growth"
    },
    {
        'question': "Which of the following is NOT one of Alderfer's ERG Theory?",
        'options': ["Existence", "Relatedness", "Growth", "Equity"],
        'answer': "Equity"
    },
            # Add more questions related to motivation theories
        ]
        
        
        motivation_answers = display_quiz(motivation_questions)

        if st.button("Submit Motivation Answers"):
            motivation_score = calculate_score(motivation_answers, motivation_questions)
            st.write(f"Your score for Motivation Theories is: {motivation_score}/{len(motivation_questions)}")

    with st.expander("Emotions"):
        emotions_questions = [
            {
                'question': "What is the James-Lange theory of emotion?",
                'options': ["Emotions are the result of the physiological reactions to stimuli", "Emotions are caused by cognitive appraisal of events", "Emotions are culturally determined", "Emotions are primarily expressions of biological instincts"],
                'answer': "Emotions are the result of the physiological reactions to stimuli"
            },
            {
        'question': "According to the Cannon-Bard theory of emotion, which of the following occurs simultaneously?",
        'options': ["Physiological arousal and emotional experience", "Physiological arousal followed by emotional experience", "Emotional experience followed by physiological arousal", "Physiological arousal without emotional experience"],
        'answer': "Physiological arousal and emotional experience"
    },
    {
        'question': "The Schachter-Singer two-factor theory of emotion suggests that emotions involve:",
        'options': ["Physiological arousal and cognitive interpretation", "Biological instincts", "Social learning and cultural factors", "Emotional expression and nonverbal communication"],
        'answer': "Physiological arousal and cognitive interpretation"
    },
    {
        'question': "Which theory suggests that emotional experiences depend on how we interpret bodily responses rather than on the nature of the stimulus?",
        'options': ["Facial Feedback Hypothesis", "Cognitive Appraisal Theory", "Emotion-Focused Coping Theory", "Emotion Regulation Theory"],
        'answer': "Facial Feedback Hypothesis"
    },
    {
        'question': "According to Lazarus' Cognitive-Mediational Theory, emotions arise from:",
        'options': ["Conscious evaluations of events", "Physiological responses to stimuli", "Biological instincts", "Nonconscious processes"],
        'answer': "Conscious evaluations of events"
    },
            # Add more questions related to emotions
        ]
        emotions_answers = display_quiz(emotions_questions)

        if st.button("Submit Emotions Answers"):
            emotions_score = calculate_score(emotions_answers, emotions_questions)
            st.write(f"Your score for Emotions is: {emotions_score}/{len(emotions_questions)}")

if __name__ == "__main__":
    main()
