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

batch_data = {
    4: { # Hobbies
        "grammar_affirmative": [{"en": "I like reading books.", "vi": "Tôi thích đọc sách."}, {"en": "He plays the guitar.", "vi": "Anh ấy chơi đàn guitar."}, {"en": "They love swimming.", "vi": "Họ yêu thích bơi lội."}],
        "grammar_negative": [{"en": "I don't like dancing.", "vi": "Tôi không thích nhảy múa."}, {"en": "She doesn't play soccer.", "vi": "Cô ấy không chơi bóng đá."}, {"en": "We don't watch TV.", "vi": "Chúng tôi không xem tivi."}],
        "vocabulary": [
            {"word": "Hobby", "phonetic": "/ˈhɑː.bi/", "meaning": "Sở thích", "example": "Reading is my hobby.", "exampleVi": "Đọc sách là sở thích của tôi."},
            {"word": "Reading", "phonetic": "/ˈriː.dɪŋ/", "meaning": "Đọc sách", "example": "I like reading.", "exampleVi": "Tôi thích đọc sách."},
            {"word": "Music", "phonetic": "/ˈmjuː.zɪk/", "meaning": "Âm nhạc", "example": "I listen to music.", "exampleVi": "Tôi nghe nhạc."},
            {"word": "Cooking", "phonetic": "/ˈkʊk.ɪŋ/", "meaning": "Nấu ăn", "example": "Cooking is fun.", "exampleVi": "Nấu ăn rất vui."},
            {"word": "Sports", "phonetic": "/spɔːrts/", "meaning": "Thể thao", "example": "I play sports.", "exampleVi": "Tôi chơi thể thao."},
            {"word": "Travel", "phonetic": "/ˈtræv.əl/", "meaning": "Du lịch", "example": "I love to travel.", "exampleVi": "Tôi yêu du lịch."},
            {"word": "Photography", "phonetic": "/fəˈtɑː.ɡrə.fi/", "meaning": "Nhiếp ảnh", "example": "I like photography.", "exampleVi": "Tôi thích nhiếp ảnh."},
            {"word": "Painting", "phonetic": "/ˈpeɪn.tɪŋ/", "meaning": "Hội họa", "example": "Painting is relaxing.", "exampleVi": "Vẽ tranh rất thư giãn."},
            {"word": "Dancing", "phonetic": "/ˈdæn.sɪŋ/", "meaning": "Nhảy múa", "example": "She enjoys dancing.", "exampleVi": "Cô ấy thích nhảy múa."},
            {"word": "Gaming", "phonetic": "/ˈɡeɪ.mɪŋ/", "meaning": "Chơi game", "example": "Gaming is popular.", "exampleVi": "Chơi game rất phổ biến."}
        ],
        "listening": [{"en": "What are your hobbies?", "vi": "Sở thích của bạn là gì?"}, {"en": "I like listening to music.", "vi": "Tôi thích nghe nhạc."}, {"en": "My brother loves playing soccer.", "vi": "Anh trai tôi yêu bóng đá."}, {"en": "She enjoys cooking for her family.", "vi": "Cô ấy thích nấu ăn cho gia đình."}, {"en": "We go swimming every weekend.", "vi": "Chúng tôi đi bơi mỗi cuối tuần."}, {"en": "I take photos in the park.", "vi": "Tôi chụp ảnh trong công viên."}, {"en": "He spends time gaming.", "vi": "Anh ấy dành thời gian chơi game."}, {"en": "Do you like reading books?", "vi": "Bạn có thích đọc sách không?"}, {"en": "Yes, I read every night.", "vi": "Vâng, tôi đọc mỗi tối."}, {"en": "Traveling is very exciting.", "vi": "Du lịch rất thú vị."}],
        "speaking": [{"en": "Do you have any hobbies?", "vi": "Bạn có sở thích nào không?"}, {"en": "Yes, I like reading.", "vi": "Có, tôi thích đọc sách."}, {"en": "What kind of books?", "vi": "Loại sách gì?"}, {"en": "I like novels.", "vi": "Tôi thích tiểu thuyết."}, {"en": "I don't like sports.", "vi": "Tôi không thích thể thao."}, {"en": "How about music?", "vi": "Còn âm nhạc thì sao?"}, {"en": "I love pop music.", "vi": "Tôi yêu nhạc pop."}, {"en": "She plays the piano.", "vi": "Cô ấy chơi piano."}, {"en": "I want to travel more.", "vi": "Tôi muốn đi du lịch nhiều hơn."}, {"en": "That sounds great!", "vi": "Nghe có vẻ tuyệt vời!"}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I like _____ books.", "answer": "reading", "hint": "đọc"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My _____ is music.", "answer": "hobby", "hint": "sở thích"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I love to _____.", "answer": "travel", "hint": "du lịch"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She enjoys _____.", "answer": "cooking", "hint": "nấu ăn"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I play _____.", "answer": "sports", "hint": "thể thao"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I listen to _____.", "answer": "music", "hint": "âm nhạc"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He likes _____.", "answer": "gaming", "hint": "chơi game"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I like _____ photos.", "answer": "taking", "hint": "chụp (ảnh)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Painting is _____.", "answer": "relaxing", "hint": "thư giãn"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "We like _____.", "answer": "dancing", "hint": "nhảy múa"}],
        "quizzes": [{"question": "'Hobby' nghĩa là gì?", "options": ["Công việc", "Sở thích", "Học tập", "Nghỉ ngơi"], "correct": 1}, {"question": "I like _____ music.", "options": ["listen", "listening", "to listen", "listened"], "correct": 1}, {"question": "She _____ play soccer.", "options": ["don't", "doesn't", "isn't", "not"], "correct": 1}, {"question": "Do you have _____ hobbies?", "options": ["any", "some", "a", "an"], "correct": 0}, {"question": "He _____ reading.", "options": ["like", "likes", "liking", "liked"], "correct": 1}, {"question": "They _____ watch TV.", "options": ["don't", "doesn't", "isn't", "aren't"], "correct": 0}, {"question": "Cooking _____ fun.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "'Travel' nghĩa là gì?", "options": ["Làm việc", "Đi lại", "Du lịch", "Mua sắm"], "correct": 2}, {"question": "I _____ photography.", "options": ["like", "likes", "am like", "liking"], "correct": 0}, {"question": "What _____ your hobbies?", "options": ["is", "am", "are", "do"], "correct": 2}]
    },
    5: { # Jobs
        "grammar_affirmative": [{"en": "I am a doctor.", "vi": "Tôi là một bác sĩ."}, {"en": "She works at a bank.", "vi": "Cô ấy làm việc tại ngân hàng."}, {"en": "A teacher teaches students.", "vi": "Một giáo viên dạy học sinh."}],
        "grammar_negative": [{"en": "I don't work in a factory.", "vi": "Tôi không làm việc ở nhà máy."}, {"en": "He is not a pilot.", "vi": "Anh ấy không phải là phi công."}, {"en": "They don't have a job.", "vi": "Họ không có việc làm."}],
        "vocabulary": [
            {"word": "Job", "phonetic": "/dʒɑːb/", "meaning": "Công việc", "example": "What is your job?", "exampleVi": "Công việc của bạn là gì?"},
            {"word": "Doctor", "phonetic": "/ˈdɑːk.tɚ/", "meaning": "Bác sĩ", "example": "The doctor helps people.", "exampleVi": "Bác sĩ giúp đỡ mọi người."},
            {"word": "Teacher", "phonetic": "/ˈtiː.tʃɚ/", "meaning": "Giáo viên", "example": "My teacher is nice.", "exampleVi": "Giáo viên của tôi rất tốt."},
            {"word": "Nurse", "phonetic": "/nɝːs/", "meaning": "Y tá", "example": "The nurse is kind.", "exampleVi": "Y tá rất tử tế."},
            {"word": "Engineer", "phonetic": "/ˌen.dʒɪˈnɪr/", "meaning": "Kỹ sư", "example": "He is an engineer.", "exampleVi": "Anh ấy là kỹ sư."},
            {"word": "Police officer", "phonetic": "/pəˈliːs ˌɑː.fɪ.sɚ/", "meaning": "Cảnh sát", "example": "The police officer is brave.", "exampleVi": "Cảnh sát rất dũng cảm."},
            {"word": "Chef", "phonetic": "/ʃef/", "meaning": "Đầu bếp", "example": "The chef cooks food.", "exampleVi": "Đầu bếp nấu ăn."},
            {"word": "Farmer", "phonetic": "/ˈfɑːr.mɚ/", "meaning": "Nông dân", "example": "The farmer works hard.", "exampleVi": "Nông dân làm việc chăm chỉ."},
            {"word": "Driver", "phonetic": "/ˈdraɪ.vɚ/", "meaning": "Tài xế", "example": "The driver is careful.", "exampleVi": "Tài xế rất cẩn thận."},
            {"word": "Artist", "phonetic": "/ˈɑːr.tɪst/", "meaning": "Họa sĩ", "example": "The artist paints.", "exampleVi": "Họa sĩ vẽ tranh."}
        ],
        "listening": [{"en": "What do you do?", "vi": "Bạn làm nghề gì?"}, {"en": "I am a doctor.", "vi": "Tôi là bác sĩ."}, {"en": "Where do you work?", "vi": "Bạn làm việc ở đâu?"}, {"en": "I work in a hospital.", "vi": "Tôi làm việc ở bệnh viện."}, {"en": "My sister is a nurse.", "vi": "Em gái tôi là y tá."}, {"en": "He is a famous chef.", "vi": "Anh ấy là một đầu bếp nổi tiếng."}, {"en": "The teacher is in the classroom.", "vi": "Giáo viên đang ở trong lớp."}, {"en": "Does he work at a farm?", "vi": "Anh ấy có làm việc ở trang trại không?"}, {"en": "No, he is an engineer.", "vi": "Không, anh ấy là kỹ sư."}, {"en": "Being a driver is hard.", "vi": "Làm tài xế rất vất vả."}],
        "speaking": [{"en": "What is your father's job?", "vi": "Công việc của bố bạn là gì?"}, {"en": "He is a farmer.", "vi": "Ông ấy là nông dân."}, {"en": "How about your mother?", "vi": "Còn mẹ bạn thì sao?"}, {"en": "She is an artist.", "vi": "Bà ấy là họa sĩ."}, {"en": "I want to be a teacher.", "vi": "Tôi muốn trở thành giáo viên."}, {"en": "Why?", "vi": "Tại sao?"}, {"en": "Because I love children.", "vi": "Vì tôi yêu trẻ em."}, {"en": "He is a police officer.", "vi": "Anh ấy là cảnh sát."}, {"en": "She is a chef.", "vi": "Cô ấy là đầu bếp."}, {"en": "That's a cool job!", "vi": "Đó là một công việc tuyệt vời!"}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am a _____.", "answer": "doctor", "hint": "bác sĩ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She works as a _____.", "answer": "nurse", "hint": "y tá"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is an _____.", "answer": "engineer", "hint": "kỹ sư"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "My father is a _____.", "answer": "farmer", "hint": "nông dân"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ paints pictures.", "answer": "artist", "hint": "họa sĩ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ cooks food.", "answer": "chef", "hint": "đầu bếp"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "What is your _____?", "answer": "job", "hint": "công việc"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is a _____ officer.", "answer": "police", "hint": "cảnh sát (police...)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ drives a bus.", "answer": "driver", "hint": "tài xế"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I work at a _____.", "answer": "hospital", "hint": "bệnh viện"}],
        "quizzes": [{"question": "'Chef' nghĩa là gì?", "options": ["Bác sĩ", "Y tá", "Đầu bếp", "Kỹ sư"], "correct": 2}, {"question": "What _____ you do?", "options": ["do", "does", "is", "are"], "correct": 0}, {"question": "He _____ in a bank.", "options": ["work", "works", "working", "worked"], "correct": 1}, {"question": "I am _____ engineer.", "options": ["a", "an", "the", "some"], "correct": 1}, {"question": "She _____ a nurse.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "My father _____ work at a school.", "options": ["don't", "doesn't", "isn't", "not"], "correct": 1}, {"question": "The _____ helps patients.", "options": ["teacher", "doctor", "chef", "farmer"], "correct": 1}, {"question": "'Farmer' nghĩa là gì?", "options": ["Nông dân", "Công nhân", "Kỹ sư", "Bác sĩ"], "correct": 0}, {"question": "Does she _____ as a teacher?", "options": ["work", "works", "working", "worked"], "correct": 0}, {"question": "They _____ have a job.", "options": ["don't", "doesn't", "isn't", "not"], "correct": 0}]
    }
}

for d in batch_data:
    update_lesson(d, batch_data[d])
