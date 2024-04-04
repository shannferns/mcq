pip install streamlit

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
    st.title("MCQ Quiz App")

    # Define collapsible sections for different topics
    with st.beta_expander("Motivation Theories"):
        motivation_questions = [
            {
                'question': "What is the need hierarchy theory proposed by Abraham Maslow?",
                'options': ["Physiological, Safety, Social, Esteem, Self-actualization", "Social, Esteem, Self-actualization, Physiological, Safety", "Self-actualization, Esteem, Social, Safety, Physiological", "Safety, Physiological, Esteem, Self-actualization, Social"],
                'answer': "Physiological, Safety, Social, Esteem, Self-actualization"
            },
            # Add more questions related to motivation theories
        ]
        motivation_answers = display_quiz(motivation_questions)

        if st.button("Submit Motivation Answers"):
            motivation_score = calculate_score(motivation_answers, motivation_questions)
            st.write(f"Your score for Motivation Theories is: {motivation_score}/{len(motivation_questions)}")

    with st.beta_expander("Emotions"):
        emotions_questions = [
            {
                'question': "What is the James-Lange theory of emotion?",
                'options': ["Emotions are the result of the physiological reactions to stimuli", "Emotions are caused by cognitive appraisal of events", "Emotions are culturally determined", "Emotions are primarily expressions of biological instincts"],
                'answer': "Emotions are the result of the physiological reactions to stimuli"
            },
            # Add more questions related to emotions
        ]
        emotions_answers = display_quiz(emotions_questions)

        if st.button("Submit Emotions Answers"):
            emotions_score = calculate_score(emotions_answers, emotions_questions)
            st.write(f"Your score for Emotions is: {emotions_score}/{len(emotions_questions)}")

if __name__ == "__main__":
    main()
