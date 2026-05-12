import json
import os

data_dir = r"d:\WEBHOCTA\webhoctienganhmoingay\data\lessons"

def update_lesson(day, data):
    file_path = os.path.join(data_dir, f"day{day}.json")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    
    # Update grammar examples (3 each)
    if "tense" in lesson and "rules" in lesson["tense"]:
        # Assuming rule 0 is Khẳng định and rule 1 is Phủ định
        if len(lesson["tense"]["rules"]) >= 2:
            lesson["tense"]["rules"][0]["examples"] = data["grammar_affirmative"]
            lesson["tense"]["rules"][1]["examples"] = data["grammar_negative"]
    
    # Update vocabulary (10)
    lesson["vocabulary"] = []
    for i, v in enumerate(data["vocabulary"]):
        v["id"] = f"v{day}_{i+1}"
        lesson["vocabulary"].append(v)
    
    # Update listening (10)
    lesson["listening"] = []
    for i, s in enumerate(data["listening"]):
        lesson["listening"].append({"id": f"l{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]})
    
    # Update speaking (10)
    lesson["speaking"] = []
    for i, s in enumerate(data["speaking"]):
        lesson["speaking"].append({"id": f"s{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]})
        
    # Update writing (10)
    lesson["writing"] = []
    for i, w in enumerate(data["writing"]):
        w["id"] = f"w{day}_{i+1}"
        lesson["writing"].append(w)
        
    # Update quizzes (10-15)
    lesson["quizzes"] = []
    for i, q in enumerate(data["quizzes"]):
        q["id"] = f"q{day}_{i+1}"
        lesson["quizzes"].append(q)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)
    print(f"Updated Day {day}")

# Data for Day 1
day1_data = {
    "grammar_affirmative": [
        {"en": "I am a student.", "vi": "Tôi là một học sinh."},
        {"en": "My name is Lan.", "vi": "Tên tôi là Lan."},
        {"en": "I come from Vietnam.", "vi": "Tôi đến từ Việt Nam."}
    ],
    "grammar_negative": [
        {"en": "I am not a teacher.", "vi": "Tôi không phải là giáo viên."},
        {"en": "I don't live in Japan.", "vi": "Tôi không sống ở Nhật Bản."},
        {"en": "My name is not Mary.", "vi": "Tên tôi không phải là Mary."}
    ],
    "vocabulary": [
        {"word": "Hello", "phonetic": "/həˈloʊ/", "meaning": "Xin chào", "example": "Hello, how are you?", "exampleVi": "Xin chào, bạn khỏe không?"},
        {"word": "Goodbye", "phonetic": "/ɡʊdˈbaɪ/", "meaning": "Tạm biệt", "example": "Goodbye, see you later.", "exampleVi": "Tạm biệt, hẹn gặp lại sau."},
        {"word": "Name", "phonetic": "/neɪm/", "meaning": "Tên", "example": "My name is Peter.", "exampleVi": "Tên tôi là Peter."},
        {"word": "Age", "phonetic": "/eɪdʒ/", "meaning": "Tuổi", "example": "What is your age?", "exampleVi": "Tuổi của bạn là bao nhiêu?"},
        {"word": "Country", "phonetic": "/ˈkʌn.tri/", "meaning": "Quốc gia", "example": "Which country are you from?", "exampleVi": "Bạn đến từ quốc gia nào?"},
        {"word": "Meet", "phonetic": "/miːt/", "meaning": "Gặp gỡ", "example": "Nice to meet you.", "exampleVi": "Rất vui được gặp bạn."},
        {"word": "Fine", "phonetic": "/faɪn/", "meaning": "Khỏe/Tốt", "example": "I am fine, thank you.", "exampleVi": "Tôi khỏe, cảm ơn bạn."},
        {"word": "Friend", "phonetic": "/frend/", "meaning": "Bạn bè", "example": "He is my friend.", "exampleVi": "Anh ấy là bạn của tôi."},
        {"word": "Teacher", "phonetic": "/ˈtiː.tʃɚ/", "meaning": "Giáo viên", "example": "I am a teacher.", "exampleVi": "Tôi là một giáo viên."},
        {"word": "Student", "phonetic": "/ˈstuː.dənt/", "meaning": "Học sinh", "example": "She is a student.", "exampleVi": "Cô ấy là một học sinh."}
    ],
    "listening": [
        {"en": "Hello, my name is John.", "vi": "Xin chào, tên tôi là John."},
        {"en": "How are you doing today?", "vi": "Hôm nay bạn thế nào?"},
        {"en": "I am from the United States.", "vi": "Tôi đến từ Hoa Kỳ."},
        {"en": "Nice to meet you all.", "vi": "Rất vui được gặp tất cả các bạn."},
        {"en": "I am twenty years old.", "vi": "Tôi hai mươi tuổi."},
        {"en": "Goodbye, have a nice day.", "vi": "Tạm biệt, chúc một ngày tốt lành."},
        {"en": "This is my friend, Mary.", "vi": "Đây là bạn của tôi, Mary."},
        {"en": "Are you a student here?", "vi": "Bạn có phải là học sinh ở đây không?"},
        {"en": "I am very happy today.", "vi": "Hôm nay tôi rất hạnh phúc."},
        {"en": "See you again tomorrow.", "vi": "Hẹn gặp lại bạn vào ngày mai."}
    ],
    "speaking": [
        {"en": "Hello!", "vi": "Xin chào!"},
        {"en": "My name is Lan.", "vi": "Tên tôi là Lan."},
        {"en": "I am from Vietnam.", "vi": "Tôi đến từ Việt Nam."},
        {"en": "I am a student.", "vi": "Tôi là học sinh."},
        {"en": "I am eighteen years old.", "vi": "Tôi 18 tuổi."},
        {"en": "How about you?", "vi": "Còn bạn thì sao?"},
        {"en": "Nice to meet you.", "vi": "Rất vui được gặp bạn."},
        {"en": "I am fine, thanks.", "vi": "Tôi khỏe, cảm ơn."},
        {"en": "Goodbye!", "vi": "Tạm biệt!"},
        {"en": "See you later.", "vi": "Hẹn gặp lại sau."}
    ],
    "writing": [
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is Lan.", "answer": "name", "hint": "Tên"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____ Vietnam.", "answer": "from", "hint": "đến từ"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Nice to _____ you.", "answer": "meet", "hint": "gặp"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "How _____ you?", "answer": "are", "hint": "thì/là/ở"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I _____ a student.", "answer": "am", "hint": "thì/là/ở"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Goodbye, _____ you later.", "answer": "see", "hint": "hẹn gặp"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____ years old.", "answer": "twenty", "hint": "20"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is my _____.", "answer": "friend", "hint": "bạn"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____, thank you.", "answer": "fine", "hint": "khỏe"},
        {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Which _____ are you from?", "answer": "country", "hint": "quốc gia"}
    ],
    "quizzes": [
        {"question": "'Hello' nghĩa là gì?", "options": ["Xin chào", "Tạm biệt", "Cảm ơn", "Xin lỗi"], "correct": 0},
        {"question": "'Goodbye' nghĩa là gì?", "options": ["Xin chào", "Tạm biệt", "Cảm ơn", "Xin lỗi"], "correct": 1},
        {"question": "How _____ you?", "options": ["is", "am", "are", "do"], "correct": 2},
        {"question": "I _____ a student.", "options": ["is", "am", "are", "be"], "correct": 1},
        {"question": "My _____ is John.", "options": ["age", "name", "country", "friend"], "correct": 1},
        {"question": "Nice to _____ you.", "options": ["see", "meet", "greet", "look"], "correct": 1},
        {"question": "I am _____ Vietnam.", "options": ["at", "on", "from", "in"], "correct": 2},
        {"question": "_____ to meet you.", "options": ["Good", "Nice", "Well", "Fine"], "correct": 1},
        {"question": "How old _____ she?", "options": ["is", "am", "are", "be"], "correct": 0},
        {"question": "See you _____.", "options": ["later", "after", "then", "now"], "correct": 0}
    ]
}

# Apply to Day 1
update_lesson(1, day1_data)
