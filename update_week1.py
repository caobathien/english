import json
import os

data_dir = r"d:\WEBHOCTA\webhoctienganhmoingay\data\lessons"

def update_lesson(day, data):
    file_path = os.path.join(data_dir, f"day{day}.json")
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    if "tense" in lesson and "rules" in lesson["tense"] and len(lesson["tense"]["rules"]) >= 2:
        lesson["tense"]["rules"][0]["examples"] = data["grammar_affirmative"]
        lesson["tense"]["rules"][1]["examples"] = data["grammar_negative"]
    lesson["vocabulary"] = [{"id": f"v{day}_{i+1}", **v} for i, v in enumerate(data["vocabulary"])]
    lesson["listening"] = [{"id": f"l{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]} for i, s in enumerate(data["listening"])]
    lesson["speaking"] = [{"id": f"s{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]} for i, s in enumerate(data["speaking"])]
    lesson["writing"] = [{"id": f"w{day}_{i+1}", **w} for i, w in enumerate(data["writing"])]
    lesson["quizzes"] = [{"id": f"q{day}_{i+1}", **q} for i, q in enumerate(data["quizzes"])]
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)
    print(f"Updated Day {day}")

# Data for Week 1 (Day 2-7)
week1_data = {
    2: { # Family & Friends
        "grammar_affirmative": [{"en": "He is my brother.", "vi": "Anh ấy là anh trai tôi."}, {"en": "She has a big family.", "vi": "Cô ấy có một gia đình lớn."}, {"en": "My friends are kind.", "vi": "Những người bạn của tôi rất tử tế."}],
        "grammar_negative": [{"en": "I don't have a sister.", "vi": "Tôi không có chị/em gái."}, {"en": "He isn't my cousin.", "vi": "Anh ấy không phải là anh em họ của tôi."}, {"en": "They aren't my friends.", "vi": "Họ không phải là bạn của tôi."}],
        "vocabulary": [
            {"word": "Family", "phonetic": "/ˈfæm.əl.i/", "meaning": "Gia đình", "example": "I love my family.", "exampleVi": "Tôi yêu gia đình mình."},
            {"word": "Father", "phonetic": "/ˈfɑː.ðɚ/", "meaning": "Bố", "example": "My father is a doctor.", "exampleVi": "Bố tôi là bác sĩ."},
            {"word": "Mother", "phonetic": "/ˈmʌð.ɚ/", "meaning": "Mẹ", "example": "My mother is a teacher.", "exampleVi": "Mẹ tôi là giáo viên."},
            {"word": "Brother", "phonetic": "/ˈbrʌð.ɚ/", "meaning": "Anh/Em trai", "example": "I have one brother.", "exampleVi": "Tôi có một người anh/em trai."},
            {"word": "Sister", "phonetic": "/ˈsɪs.tɚ/", "meaning": "Chị/Em gái", "example": "She is my younger sister.", "exampleVi": "Cô ấy là em gái tôi."},
            {"word": "Friend", "phonetic": "/frend/", "meaning": "Bạn bè", "example": "He is my best friend.", "exampleVi": "Anh ấy là bạn thân của tôi."},
            {"word": "Cousin", "phonetic": "/ˈkʌz.ən/", "meaning": "Anh em họ", "example": "My cousin lives in Hanoi.", "exampleVi": "Anh em họ tôi sống ở Hà Nội."},
            {"word": "Parents", "phonetic": "/ˈper.ənts/", "meaning": "Bố mẹ", "example": "My parents are great.", "exampleVi": "Bố mẹ tôi tuyệt vời."},
            {"word": "Grandfather", "phonetic": "/ˈɡræn.fɑː.ðɚ/", "meaning": "Ông", "example": "My grandfather is 70.", "exampleVi": "Ông tôi 70 tuổi."},
            {"word": "Grandmother", "phonetic": "/ˈɡræn.mʌð.ɚ/", "meaning": "Bà", "example": "My grandmother is kind.", "exampleVi": "Bà tôi tốt bụng."}
        ],
        "listening": [{"en": "This is my family.", "vi": "Đây là gia đình tôi."}, {"en": "I have two brothers.", "vi": "Tôi có hai người anh em trai."}, {"en": "My sister is a student.", "vi": "Em gái tôi là học sinh."}, {"en": "How many people are in your family?", "vi": "Có bao nhiêu người trong gia đình bạn?"}, {"en": "My father is very tall.", "vi": "Bố tôi rất cao."}, {"en": "Do you have any siblings?", "vi": "Bạn có anh chị em nào không?"}, {"en": "My mother loves cooking.", "vi": "Mẹ tôi thích nấu ăn."}, {"en": "I live with my parents.", "vi": "Tôi sống cùng bố mẹ."}, {"en": "He is my favorite cousin.", "vi": "Anh ấy là người anh họ tôi yêu thích nhất."}, {"en": "We are best friends.", "vi": "Chúng tôi là bạn thân."}],
        "speaking": [{"en": "Who is this?", "vi": "Đây là ai?"}, {"en": "He is my father.", "vi": "Ông ấy là bố tôi."}, {"en": "She is my mother.", "vi": "Bà ấy là mẹ tôi."}, {"en": "I have a sister.", "vi": "Tôi có một người chị/em gái."}, {"en": "I don't have a brother.", "vi": "Tôi không có anh/em trai."}, {"en": "My parents are happy.", "vi": "Bố mẹ tôi đang hạnh phúc."}, {"en": "Are you his friend?", "vi": "Bạn có phải là bạn của anh ấy không?"}, {"en": "Yes, I am.", "vi": "Vâng, đúng vậy."}, {"en": "I love my family.", "vi": "Tôi yêu gia đình mình."}, {"en": "This is my best friend.", "vi": "Đây là bạn thân nhất của tôi."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I have one _____.", "answer": "brother", "hint": "anh/em trai"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is my _____.", "answer": "sister", "hint": "chị/em gái"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is a doctor.", "answer": "father", "hint": "bố"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I live with my _____.", "answer": "parents", "hint": "bố mẹ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is my _____.", "answer": "friend", "hint": "bạn"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is kind.", "answer": "grandmother", "hint": "bà"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "How many _____?", "answer": "people", "hint": "người"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ my family.", "answer": "love", "hint": "yêu"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is my _____.", "answer": "cousin", "hint": "anh em họ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is 70.", "answer": "grandfather", "hint": "ông"}],
        "quizzes": [{"question": "'Mother' nghĩa là gì?", "options": ["Bố", "Mẹ", "Anh", "Em"], "correct": 1}, {"question": "I _____ two sisters.", "options": ["has", "have", "am", "do"], "correct": 1}, {"question": "He _____ my brother.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "Who is _____?", "options": ["this", "these", "those", "that"], "correct": 0}, {"question": "My _____ are great.", "options": ["parent", "parents", "parentes", "parent's"], "correct": 1}, {"question": "She is my _____.", "options": ["brother", "sister", "father", "son"], "correct": 1}, {"question": "'Friend' nghĩa là gì?", "options": ["Bạn", "Thù", "Người thân", "Người lạ"], "correct": 0}, {"question": "Are they _____?", "options": ["your friend", "your friends", "you friends", "yours friends"], "correct": 1}, {"question": "My father _____ a doctor.", "options": ["am", "is", "are", "be"], "correct": 1}, {"question": "I love _____ family.", "options": ["my", "me", "mine", "I"], "correct": 0}]
    },
    3: { # Daily Routine
        "grammar_affirmative": [{"en": "I wake up at 7 AM.", "vi": "Tôi thức dậy lúc 7 giờ sáng."}, {"en": "She brushes her teeth.", "vi": "Cô ấy đánh răng."}, {"en": "We have lunch at noon.", "vi": "Chúng tôi ăn trưa lúc giữa trưa."}],
        "grammar_negative": [{"en": "I don't go to bed late.", "vi": "Tôi không đi ngủ muộn."}, {"en": "He doesn't eat breakfast.", "vi": "Anh ấy không ăn sáng."}, {"en": "They don't work on Sundays.", "vi": "Họ không làm việc vào Chủ nhật."}],
        "vocabulary": [
            {"word": "Wake up", "phonetic": "/weɪk ʌp/", "meaning": "Thức dậy", "example": "I wake up early.", "exampleVi": "Tôi thức dậy sớm."},
            {"word": "Breakfast", "phonetic": "/ˈbrek.fəst/", "meaning": "Bữa sáng", "example": "I eat breakfast at 8 AM.", "exampleVi": "Tôi ăn sáng lúc 8 giờ."},
            {"word": "Brush", "phonetic": "/brʌʃ/", "meaning": "Chải/Đánh", "example": "I brush my teeth.", "exampleVi": "Tôi đánh răng."},
            {"word": "Wash", "phonetic": "/wɑːʃ/", "meaning": "Rửa", "example": "Wash your hands.", "exampleVi": "Hãy rửa tay của bạn."},
            {"word": "Lunch", "phonetic": "/lʌntʃ/", "meaning": "Bữa trưa", "example": "We have lunch at 12.", "exampleVi": "Chúng tôi ăn trưa lúc 12 giờ."},
            {"word": "Dinner", "phonetic": "/ˈdɪn.ɚ/", "meaning": "Bữa tối", "example": "I cook dinner.", "exampleVi": "Tôi nấu bữa tối."},
            {"word": "Shower", "phonetic": "/ˈʃaʊ.ɚ/", "meaning": "Tắm vòi sen", "example": "I take a shower.", "exampleVi": "Tôi đi tắm."},
            {"word": "Work", "phonetic": "/wɝːk/", "meaning": "Làm việc", "example": "I go to work.", "exampleVi": "Tôi đi làm."},
            {"word": "Sleep", "phonetic": "/sliːp/", "meaning": "Ngủ", "example": "I sleep 8 hours.", "exampleVi": "Tôi ngủ 8 tiếng."},
            {"word": "Exercise", "phonetic": "/ˈek.sɚ.saɪz/", "meaning": "Tập thể dục", "example": "I exercise every day.", "exampleVi": "Tôi tập thể dục mỗi ngày."}
        ],
        "listening": [{"en": "I wake up at 6 AM.", "vi": "Tôi thức dậy lúc 6 giờ sáng."}, {"en": "I have breakfast with my family.", "vi": "Tôi ăn sáng cùng gia đình."}, {"en": "Then I go to school.", "vi": "Sau đó tôi đi học."}, {"en": "I have lunch at school.", "vi": "Tôi ăn trưa ở trường."}, {"en": "I come home at 4 PM.", "vi": "Tôi về nhà lúc 4 giờ chiều."}, {"en": "I do my homework.", "vi": "Tôi làm bài tập về nhà."}, {"en": "I take a shower before dinner.", "vi": "Tôi đi tắm trước bữa tối."}, {"en": "We eat dinner at 7 PM.", "vi": "Chúng tôi ăn tối lúc 7 giờ tối."}, {"en": "I watch TV for one hour.", "vi": "Tôi xem tivi trong một tiếng."}, {"en": "I go to bed at 10 PM.", "vi": "Tôi đi ngủ lúc 10 giờ tối."}],
        "speaking": [{"en": "When do you wake up?", "vi": "Bạn thức dậy khi nào?"}, {"en": "I wake up at 7.", "vi": "Tôi thức dậy lúc 7 giờ."}, {"en": "Do you eat breakfast?", "vi": "Bạn có ăn sáng không?"}, {"en": "Yes, I do.", "vi": "Vâng, tôi có."}, {"en": "I drink milk.", "vi": "Tôi uống sữa."}, {"en": "I go to work by bus.", "vi": "Tôi đi làm bằng xe buýt."}, {"en": "What do you do in the evening?", "vi": "Bạn làm gì vào buổi tối?"}, {"en": "I relax.", "vi": "Tôi thư giãn."}, {"en": "I go to bed early.", "vi": "Tôi đi ngủ sớm."}, {"en": "Good night!", "vi": "Chúc ngủ ngon!"}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ up at 6.", "answer": "wake", "hint": "thức dậy"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I eat _____ at 8.", "answer": "breakfast", "hint": "bữa sáng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ my teeth.", "answer": "brush", "hint": "đánh (răng)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ to work.", "answer": "go", "hint": "đi"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I have _____ at 12.", "answer": "lunch", "hint": "bữa trưa"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ a shower.", "answer": "take", "hint": "tắm"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I do my _____.", "answer": "homework", "hint": "bài tập"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ dinner.", "answer": "cook", "hint": "nấu"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I go to _____ at 10.", "answer": "bed", "hint": "giường/đi ngủ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ every day.", "answer": "exercise", "hint": "tập thể dục"}],
        "quizzes": [{"question": "'Breakfast' là bữa gì?", "options": ["Sáng", "Trưa", "Chiều", "Tối"], "correct": 0}, {"question": "I _____ up at 7.", "options": ["wake", "wakes", "waking", "waked"], "correct": 0}, {"question": "She _____ her teeth.", "options": ["brush", "brushes", "brushing", "brushed"], "correct": 1}, {"question": "They _____ eat breakfast.", "options": ["don't", "doesn't", "isn't", "aren't"], "correct": 0}, {"question": "Do you _____ to work?", "options": ["go", "goes", "going", "gone"], "correct": 0}, {"question": "I take a _____.", "options": ["bath", "shower", "wash", "clean"], "correct": 1}, {"question": "We have _____ at noon.", "options": ["breakfast", "lunch", "dinner", "snack"], "correct": 1}, {"question": "He _____ to bed early.", "options": ["go", "goes", "going", "gone"], "correct": 1}, {"question": "What time _____ you wake up?", "options": ["do", "does", "is", "are"], "correct": 0}, {"question": "I _____ 8 hours.", "options": ["sleep", "sleeps", "sleeping", "slept"], "correct": 0}]
    }
}

for d in week1_data:
    update_lesson(d, week1_data[d])
