import json
import os

data_dir = r"d:\WEBHOCTA\webhoctienganhmoingay\data\lessons"

def update_lesson(day, data):
    file_path = os.path.join(data_dir, f"day{day}.json")
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    
    # Grammar
    if "tense" in lesson and "rules" in lesson["tense"] and len(lesson["tense"]["rules"]) >= 2:
        lesson["tense"]["rules"][0]["examples"] = data["grammar_affirmative"]
        lesson["tense"]["rules"][1]["examples"] = data["grammar_negative"]
    elif "tense" in lesson and "rules" in lesson["tense"] and len(lesson["tense"]["rules"]) == 1:
        lesson["tense"]["rules"][0]["examples"] = data["grammar_affirmative"]

    # Vocab
    lesson["vocabulary"] = [{"id": f"v{day}_{i+1}", **v} for i, v in enumerate(data["vocabulary"])]
    
    # Skills
    lesson["listening"] = [{"id": f"l{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]} for i, s in enumerate(data["listening"])]
    lesson["speaking"] = [{"id": f"s{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]} for i, s in enumerate(data["speaking"])]
    lesson["writing"] = [{"id": f"w{day}_{i+1}", **w} for i, w in enumerate(data["writing"])]
    
    # Quizzes (10-15)
    lesson["quizzes"] = [{"id": f"q{day}_{i+1}", **q} for i, q in enumerate(data["quizzes"])]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)

all_data = {
    1: { # Greeting
        "grammar_affirmative": [{"en": "I am Lan.", "vi": "Tôi là Lan."}, {"en": "My name is Peter.", "vi": "Tên tôi là Peter."}, {"en": "I am from Vietnam.", "vi": "Tôi đến từ Việt Nam."}],
        "grammar_negative": [{"en": "I am not a teacher.", "vi": "Tôi không phải là giáo viên."}, {"en": "My name is not John.", "vi": "Tên tôi không phải là John."}, {"en": "I am not from Japan.", "vi": "Tôi không đến từ Nhật Bản."}],
        "vocabulary": [
            {"word": "Hello", "phonetic": "/həˈloʊ/", "meaning": "Xin chào", "example": "Hello, how are you?", "exampleVi": "Xin chào, bạn khỏe không?"},
            {"word": "Goodbye", "phonetic": "/ɡʊdˈbaɪ/", "meaning": "Tạm biệt", "example": "Goodbye, see you later.", "exampleVi": "Tạm biệt, hẹn gặp lại sau."},
            {"word": "Name", "phonetic": "/neɪm/", "meaning": "Tên", "example": "My name is Lan.", "exampleVi": "Tên tôi là Lan."},
            {"word": "Age", "phonetic": "/eɪdʒ/", "meaning": "Tuổi", "example": "What is your age?", "exampleVi": "Tuổi của bạn là bao nhiêu?"},
            {"word": "Country", "phonetic": "/ˈkʌn.tri/", "meaning": "Quốc gia", "example": "Vietnam is my country.", "exampleVi": "Việt Nam là đất nước của tôi."},
            {"word": "Meet", "phonetic": "/miːt/", "meaning": "Gặp gỡ", "example": "Nice to meet you.", "exampleVi": "Rất vui được gặp bạn."},
            {"word": "Fine", "phonetic": "/faɪn/", "meaning": "Khỏe/Tốt", "example": "I am fine.", "exampleVi": "Tôi khỏe."},
            {"word": "Friend", "phonetic": "/frend/", "meaning": "Bạn bè", "example": "She is my friend.", "exampleVi": "Cô ấy là bạn tôi."},
            {"word": "Teacher", "phonetic": "/ˈtiː.tʃɚ/", "meaning": "Giáo viên", "example": "He is a teacher.", "exampleVi": "Ông ấy là giáo viên."},
            {"word": "Student", "phonetic": "/ˈstuː.dənt/", "meaning": "Học sinh", "example": "I am a student.", "exampleVi": "Tôi là học sinh."}
        ],
        "listening": [{"en": "Hello everyone.", "vi": "Chào mọi người."}, {"en": "How are you today?", "vi": "Hôm nay bạn thế nào?"}, {"en": "I am fine, thank you.", "vi": "Tôi khỏe, cảm ơn."}, {"en": "My name is Lan.", "vi": "Tên tôi là Lan."}, {"en": "I come from Vietnam.", "vi": "Tôi đến từ Việt Nam."}, {"en": "I am a student.", "vi": "Tôi là học sinh."}, {"en": "Nice to meet you.", "vi": "Rất vui được gặp bạn."}, {"en": "Goodbye!", "vi": "Tạm biệt!"}, {"en": "See you tomorrow.", "vi": "Hẹn gặp lại ngày mai."}, {"en": "Have a nice day.", "vi": "Chúc một ngày tốt lành."}],
        "speaking": [{"en": "Hi!", "vi": "Chào!"}, {"en": "What is your name?", "vi": "Tên bạn là gì?"}, {"en": "My name is John.", "vi": "Tên tôi là John."}, {"en": "Where are you from?", "vi": "Bạn từ đâu tới?"}, {"en": "I am from England.", "vi": "Tôi từ nước Anh."}, {"en": "How old are you?", "vi": "Bạn bao nhiêu tuổi?"}, {"en": "I am 20 years old.", "vi": "Tôi 20 tuổi."}, {"en": "Are you a teacher?", "vi": "Bạn là giáo viên à?"}, {"en": "No, I am a student.", "vi": "Không, tôi là học sinh."}, {"en": "Bye bye!", "vi": "Tạm biệt!"}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is Lan.", "answer": "name", "hint": "Tên"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____ Vietnam.", "answer": "from", "hint": "đến từ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "How _____ you?", "answer": "are", "hint": "thì/là/ở"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Nice to _____ you.", "answer": "meet", "hint": "gặp"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Goodbye, _____ you later.", "answer": "see", "hint": "hẹn gặp"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am a _____.", "answer": "student", "hint": "học sinh"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____ years old.", "answer": "twenty", "hint": "20"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is my _____.", "answer": "friend", "hint": "bạn"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____.", "answer": "fine", "hint": "khỏe"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is a _____.", "answer": "teacher", "hint": "giáo viên"}],
        "quizzes": [{"question": "'Hello' nghĩa là gì?", "options": ["Xin chào", "Tạm biệt", "Cảm ơn", "Xin lỗi"], "correct": 0}, {"question": "I _____ from Vietnam.", "options": ["is", "am", "are", "do"], "correct": 1}, {"question": "What is your _____?", "options": ["name", "age", "country", "friend"], "correct": 0}, {"question": "How _____ you?", "options": ["is", "am", "are", "do"], "correct": 2}, {"question": "Nice to _____ you.", "options": ["see", "meet", "greet", "look"], "correct": 1}, {"question": "I _____ a teacher.", "options": ["is", "am", "are", "not"], "correct": 3}, {"question": "Where _____ you from?", "options": ["is", "am", "are", "do"], "correct": 2}, {"question": "I am 20 years _____.", "options": ["old", "age", "new", "long"], "correct": 0}, {"question": "_____ to meet you.", "options": ["Good", "Nice", "Well", "Fine"], "correct": 1}, {"question": "Goodbye, see you _____.", "options": ["later", "after", "then", "now"], "correct": 0}]
    },
    2: { # Family
        "grammar_affirmative": [{"en": "He is my father.", "vi": "Ông ấy là bố tôi."}, {"en": "She is my mother.", "vi": "Bà ấy là mẹ tôi."}, {"en": "I have two sisters.", "vi": "Tôi có hai người chị/em gái."}],
        "grammar_negative": [{"en": "I don't have a brother.", "vi": "Tôi không có anh/em trai."}, {"en": "He isn't my cousin.", "vi": "Anh ấy không phải là anh em họ của tôi."}, {"en": "They aren't my parents.", "vi": "Họ không phải là bố mẹ tôi."}],
        "vocabulary": [
            {"word": "Family", "phonetic": "/ˈfæm.əl.i/", "meaning": "Gia đình", "example": "I love my family.", "exampleVi": "Tôi yêu gia đình mình."},
            {"word": "Father", "phonetic": "/ˈfɑː.ðɚ/", "meaning": "Bố", "example": "My father is a doctor.", "exampleVi": "Bố tôi là bác sĩ."},
            {"word": "Mother", "phonetic": "/ˈmʌð.ɚ/", "meaning": "Mẹ", "example": "My mother is a teacher.", "exampleVi": "Mẹ tôi là giáo viên."},
            {"word": "Brother", "phonetic": "/ˈbrʌð.ɚ/", "meaning": "Anh/Em trai", "example": "I have one brother.", "exampleVi": "Tôi có một người anh/em trai."},
            {"word": "Sister", "phonetic": "/ˈsɪs.tɚ/", "meaning": "Chị/Em gái", "example": "She is my sister.", "exampleVi": "Cô ấy là chị/em gái tôi."},
            {"word": "Son", "phonetic": "/sʌn/", "meaning": "Con trai", "example": "He is my son.", "exampleVi": "Nó là con trai tôi."},
            {"word": "Daughter", "phonetic": "/ˈdɑː.t̬ɚ/", "meaning": "Con gái", "example": "She is my daughter.", "exampleVi": "Nó là con gái tôi."},
            {"word": "Grandparents", "phonetic": "/ˈɡræn.per.ənts/", "meaning": "Ông bà", "example": "I love my grandparents.", "exampleVi": "Tôi yêu ông bà tôi."},
            {"word": "Uncle", "phonetic": "/ˈʌŋ.kəl/", "meaning": "Chú/Bác", "example": "He is my uncle.", "exampleVi": "Ông ấy là chú/bác tôi."},
            {"word": "Aunt", "phonetic": "/ænt/", "meaning": "Cô/Dì", "example": "She is my aunt.", "exampleVi": "Bà ấy là cô/dì tôi."}
        ],
        "listening": [{"en": "This is my family photo.", "vi": "Đây là ảnh gia đình tôi."}, {"en": "My father is 50 years old.", "vi": "Bố tôi 50 tuổi."}, {"en": "My mother is very kind.", "vi": "Mẹ tôi rất tốt bụng."}, {"en": "I have a big family.", "vi": "Tôi có một gia đình lớn."}, {"en": "Do you have any brothers?", "vi": "Bạn có anh em trai nào không?"}, {"en": "No, I only have a sister.", "vi": "Không, tôi chỉ có một người em gái."}, {"en": "My uncle lives in London.", "vi": "Chú tôi sống ở Luân Đôn."}, {"en": "My grandparents are retired.", "vi": "Ông bà tôi đã nghỉ hưu."}, {"en": "Is she your daughter?", "vi": "Cô bé có phải là con gái bạn không?"}, {"en": "We are a happy family.", "vi": "Chúng tôi là một gia đình hạnh phúc."}],
        "speaking": [{"en": "Who is he?", "vi": "Ông ấy là ai?"}, {"en": "He is my father.", "vi": "Ông ấy là bố tôi."}, {"en": "Who is she?", "vi": "Bà ấy là ai?"}, {"en": "She is my sister.", "vi": "Cô ấy là chị/em gái tôi."}, {"en": "How many siblings do you have?", "vi": "Bạn có bao nhiêu anh chị em?"}, {"en": "I have one brother.", "vi": "Tôi có một anh/em trai."}, {"en": "My family is small.", "vi": "Gia đình tôi nhỏ."}, {"en": "Do you live with your parents?", "vi": "Bạn có sống cùng bố mẹ không?"}, {"en": "Yes, I do.", "vi": "Vâng, tôi có."}, {"en": "This is my aunt.", "vi": "Đây là cô/dì của tôi."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is a doctor.", "answer": "father", "hint": "bố"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I have one _____.", "answer": "brother", "hint": "anh/em trai"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is my _____.", "answer": "mother", "hint": "mẹ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I have two _____.", "answer": "sisters", "hint": "chị/em gái"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I love my _____.", "answer": "family", "hint": "gia đình"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is my _____.", "answer": "uncle", "hint": "chú/bác"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is my _____.", "answer": "aunt", "hint": "cô/dì"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is my _____.", "answer": "son", "hint": "con trai"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is my _____.", "answer": "daughter", "hint": "con gái"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I love my _____.", "answer": "grandparents", "hint": "ông bà"}],
        "quizzes": [{"question": "'Father' nghĩa là gì?", "options": ["Bố", "Mẹ", "Anh", "Chị"], "correct": 0}, {"question": "I _____ two brothers.", "options": ["has", "have", "am", "do"], "correct": 1}, {"question": "She _____ my mother.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "My _____ are retired.", "options": ["parent", "parents", "grandparents", "uncles"], "correct": 2}, {"question": "Who is _____?", "options": ["he", "she", "it", "they"], "correct": 0}, {"question": "He is my _____.", "options": ["sister", "daughter", "aunt", "son"], "correct": 3}, {"question": "Do you _____ a sister?", "options": ["has", "have", "is", "are"], "correct": 1}, {"question": "'Uncle' nghĩa là gì?", "options": ["Chú", "Cô", "Anh", "Em"], "correct": 0}, {"question": "They _____ my friends.", "options": ["isn't", "aren't", "don't", "doesn't"], "correct": 1}, {"question": "I love _____ family.", "options": ["my", "me", "mine", "I"], "correct": 0}]
    },
    3: { # Routine
        "grammar_affirmative": [{"en": "I wake up at 6.", "vi": "Tôi thức dậy lúc 6 giờ."}, {"en": "She eats breakfast.", "vi": "Cô ấy ăn sáng."}, {"en": "We go to work.", "vi": "Chúng tôi đi làm."}],
        "grammar_negative": [{"en": "I don't sleep late.", "vi": "Tôi không ngủ muộn."}, {"en": "He doesn't watch TV.", "vi": "Anh ấy không xem tivi."}, {"en": "They don't cook dinner.", "vi": "Họ không nấu bữa tối."}],
        "vocabulary": [
            {"word": "Wake up", "phonetic": "/weɪk ʌp/", "meaning": "Thức dậy", "example": "I wake up at 7.", "exampleVi": "Tôi thức dậy lúc 7 giờ."},
            {"word": "Breakfast", "phonetic": "/ˈbrek.fəst/", "meaning": "Bữa sáng", "example": "I have breakfast.", "exampleVi": "Tôi ăn sáng."},
            {"word": "Brush", "phonetic": "/brʌʃ/", "meaning": "Đánh (răng)", "example": "I brush my teeth.", "exampleVi": "Tôi đánh răng."},
            {"word": "Wash", "phonetic": "/wɑːʃ/", "meaning": "Rửa", "example": "Wash your face.", "exampleVi": "Rửa mặt."},
            {"word": "Work", "phonetic": "/wɝːk/", "meaning": "Làm việc", "example": "I go to work.", "exampleVi": "Tôi đi làm."},
            {"word": "Lunch", "phonetic": "/lʌntʃ/", "meaning": "Bữa trưa", "example": "I eat lunch at 12.", "exampleVi": "Tôi ăn trưa lúc 12 giờ."},
            {"word": "Shower", "phonetic": "/ˈʃaʊ.ɚ/", "meaning": "Tắm", "example": "I take a shower.", "exampleVi": "Tôi đi tắm."},
            {"word": "Dinner", "phonetic": "/ˈdɪn.ɚ/", "meaning": "Bữa tối", "example": "I eat dinner.", "exampleVi": "Tôi ăn tối."},
            {"word": "Bed", "phonetic": "/bed/", "meaning": "Giường/Đi ngủ", "example": "I go to bed.", "exampleVi": "Tôi đi ngủ."},
            {"word": "Exercise", "phonetic": "/ˈek.sɚ.saɪz/", "meaning": "Tập thể dục", "example": "I exercise.", "exampleVi": "Tôi tập thể dục."}
        ],
        "listening": [{"en": "I wake up at 6 every morning.", "vi": "Tôi thức dậy lúc 6 giờ mỗi sáng."}, {"en": "First, I brush my teeth.", "vi": "Đầu tiên, tôi đánh răng."}, {"en": "Then I wash my face.", "vi": "Sau đó tôi rửa mặt."}, {"en": "I have breakfast with coffee.", "vi": "Tôi ăn sáng với cà phê."}, {"en": "I go to work at 8 AM.", "vi": "Tôi đi làm lúc 8 giờ sáng."}, {"en": "I have lunch at a restaurant.", "vi": "Tôi ăn trưa ở một nhà hàng."}, {"en": "I finish work at 5 PM.", "vi": "Tôi kết thúc công việc lúc 5 giờ chiều."}, {"en": "I take a shower in the evening.", "vi": "Tôi đi tắm vào buổi tối."}, {"en": "I eat dinner with my family.", "vi": "Tôi ăn tối cùng gia đình."}, {"en": "I go to bed at 10 PM.", "vi": "Tôi đi ngủ lúc 10 giờ tối."}],
        "speaking": [{"en": "What time do you wake up?", "vi": "Bạn thức dậy lúc mấy giờ?"}, {"en": "I wake up at 7.", "vi": "Tôi thức dậy lúc 7 giờ."}, {"en": "Do you eat breakfast?", "vi": "Bạn có ăn sáng không?"}, {"en": "Yes, I eat bread.", "vi": "Vâng, tôi ăn bánh mì."}, {"en": "How do you go to work?", "vi": "Bạn đi làm bằng gì?"}, {"en": "I go by motorbike.", "vi": "Tôi đi bằng xe máy."}, {"en": "When do you have lunch?", "vi": "Khi nào bạn ăn trưa?"}, {"en": "At 12 o'clock.", "vi": "Lúc 12 giờ."}, {"en": "Do you watch TV?", "vi": "Bạn có xem tivi không?"}, {"en": "Yes, for one hour.", "vi": "Vâng, trong một tiếng."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ up at 6.", "answer": "wake", "hint": "thức dậy"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ my teeth.", "answer": "brush", "hint": "đánh (răng)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I have _____ at 8.", "answer": "breakfast", "hint": "bữa sáng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I go to _____.", "answer": "work", "hint": "làm việc"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I eat _____ at 12.", "answer": "lunch", "hint": "bữa trưa"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ a shower.", "answer": "take", "hint": "tắm (dùng take a...)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I eat _____ at 7 PM.", "answer": "dinner", "hint": "bữa tối"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I go to _____ at 10.", "answer": "bed", "hint": "đi ngủ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ every morning.", "answer": "exercise", "hint": "tập thể dục"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ my face.", "answer": "wash", "hint": "rửa"}],
        "quizzes": [{"question": "'Breakfast' là bữa gì?", "options": ["Sáng", "Trưa", "Chiều", "Tối"], "correct": 0}, {"question": "I _____ up at 7.", "options": ["wake", "wakes", "waking", "waked"], "correct": 0}, {"question": "She _____ her teeth.", "options": ["brush", "brushes", "brushing", "brushed"], "correct": 1}, {"question": "They _____ eat dinner at home.", "options": ["don't", "doesn't", "isn't", "not"], "correct": 0}, {"question": "What time _____ you go to bed?", "options": ["do", "does", "is", "are"], "correct": 0}, {"question": "He _____ lunch at 12.", "options": ["has", "have", "is", "are"], "correct": 0}, {"question": "'Work' nghĩa là gì?", "options": ["Làm việc", "Nghỉ ngơi", "Học", "Chơi"], "correct": 0}, {"question": "I _____ a shower.", "options": ["do", "make", "take", "get"], "correct": 2}, {"question": "Do you _____?", "options": ["exercise", "exercises", "exercising", "exercised"], "correct": 0}, {"question": "I _____ TV at night.", "options": ["watch", "watches", "watching", "watched"], "correct": 0}]
    }
}

for d in all_data:
    update_lesson(d, all_data[d])
