import json
import os
import random

data_dir = r"d:\WEBHOCTA\webhoctienganhmoingay\data"
lessons_dir = os.path.join(data_dir, "lessons")

os.makedirs(lessons_dir, exist_ok=True)

weeks_config = [
    {"week": 1, "days": range(1, 8), "tense": "Present Simple", "tenseVi": "Thì Hiện Tại Đơn"},
    {"week": 2, "days": range(8, 15), "tense": "Present Continuous", "tenseVi": "Thì Hiện Tại Tiếp Diễn"},
    {"week": 3, "days": range(15, 22), "tense": "Past Simple", "tenseVi": "Thì Quá Khứ Đơn"},
    {"week": 4, "days": range(22, 29), "tense": "Future Simple", "tenseVi": "Thì Tương Lai Đơn"},
    {"week": 5, "days": range(29, 31), "tense": "Review & Communication", "tenseVi": "Ôn tập & Giao tiếp"}
]

topics = [
    "Greeting & Introduce Yourself", "Family & Friends", "Daily Routine", "Hobbies & Interests", "Jobs & Occupations",
    "Food & Drinks", "Shopping", "Describing People", "Describing Places", "Travel & Holidays",
    "Weather", "Health & Body", "Sports", "Music & Movies", "Education",
    "Technology", "Animals", "Home & Furniture", "Clothes & Fashion", "Transportation",
    "Emotions", "City Life", "Nature", "Festivals", "Restaurants",
    "Social Media", "Dreams & Goals", "Culture", "Review Part 1", "Review Part 2"
]

grammar_explanations = {
    "Present Simple": {
        "name": "Present Simple", "nameVi": "Thì Hiện Tại Đơn",
        "description": "Dùng để diễn tả thói quen, sự thật hiển nhiên, và hành động lặp lại.",
        "rules": [
            {"title": "Khẳng định", "formula": "S + V(s/es)", "examples": [{"en": "I play soccer.", "vi": "Tôi chơi bóng đá."}]},
            {"title": "Phủ định", "formula": "S + do/does + not + V", "examples": [{"en": "I don't play soccer.", "vi": "Tôi không chơi bóng đá."}]}
        ]
    },
    "Present Continuous": {
        "name": "Present Continuous", "nameVi": "Thì Hiện Tại Tiếp Diễn",
        "description": "Dùng để diễn tả hành động đang diễn ra tại thời điểm nói.",
        "rules": [
            {"title": "Khẳng định", "formula": "S + am/is/are + V-ing", "examples": [{"en": "I am studying.", "vi": "Tôi đang học."}]},
            {"title": "Phủ định", "formula": "S + am/is/are + not + V-ing", "examples": [{"en": "She is not sleeping.", "vi": "Cô ấy không đang ngủ."}]}
        ]
    },
    "Past Simple": {
        "name": "Past Simple", "nameVi": "Thì Quá Khứ Đơn",
        "description": "Dùng để diễn tả hành động đã xảy ra và kết thúc trong quá khứ.",
        "rules": [
            {"title": "Khẳng định", "formula": "S + V2/ed", "examples": [{"en": "I went to school.", "vi": "Tôi đã đi học."}]},
            {"title": "Phủ định", "formula": "S + did not + V", "examples": [{"en": "He didn't go out.", "vi": "Anh ấy đã không đi chơi."}]}
        ]
    },
    "Future Simple": {
        "name": "Future Simple", "nameVi": "Thì Tương Lai Đơn",
        "description": "Dùng để diễn tả quyết định nhất thời, dự đoán không có căn cứ.",
        "rules": [
            {"title": "Khẳng định", "formula": "S + will + V", "examples": [{"en": "I will help you.", "vi": "Tôi sẽ giúp bạn."}]},
            {"title": "Phủ định", "formula": "S + will not (won't) + V", "examples": [{"en": "I won't do it.", "vi": "Tôi sẽ không làm điều đó."}]}
        ]
    },
    "Review & Communication": {
        "name": "Review & Communication", "nameVi": "Ôn tập & Giao tiếp",
        "description": "Ôn tập tổng hợp các thì đã học và luyện phản xạ giao tiếp.",
        "rules": [
            {"title": "Tổng hợp", "formula": "Present / Past / Future", "examples": [{"en": "I learn English every day. Yesterday I learned vocabulary. Tomorrow I will practice speaking.", "vi": "Tôi học tiếng Anh mỗi ngày. Hôm qua tôi đã học từ vựng. Ngày mai tôi sẽ luyện nói."}]}
        ]
    }
}

lessons_index = []

for config in weeks_config:
    week = config["week"]
    for day in config["days"]:
        title = topics[day - 1]
        file_name = f"day{day}.json"
        
        lesson_info = {
            "id": day,
            "file": file_name,
            "week": week,
            "day": day,
            "tense": {"name": grammar_explanations[config["tense"]]["name"]},
            "title": title,
            "subtitle": f"Bài học ngày {day} - {title}",
            "icon": "📚",
            "xpReward": 100
        }
        lessons_index.append(lesson_info)

        lesson_data = {
            "id": day,
            "week": week,
            "day": day,
            "title": title,
            "subtitle": f"Bài học ngày {day} - {title}",
            "icon": "📚",
            "xpReward": 100,
            "tense": grammar_explanations[config["tense"]],
            "vocabulary": [
                {
                    "id": f"v{day}_1",
                    "word": f"Word_{day}_1",
                    "phonetic": "/wɜːrd/",
                    "meaning": "Từ vựng mẫu 1",
                    "example": f"This is an example for Word_{day}_1.",
                    "exampleVi": "Đây là ví dụ cho từ mẫu 1."
                },
                {
                    "id": f"v{day}_2",
                    "word": f"Word_{day}_2",
                    "phonetic": "/wɜːrd/",
                    "meaning": "Từ vựng mẫu 2",
                    "example": f"This is an example for Word_{day}_2.",
                    "exampleVi": "Đây là ví dụ cho từ mẫu 2."
                }
            ],
            "listening": [
                { "id": f"l{day}_1", "sentence": "I like studying English.", "sentenceVi": "Tôi thích học tiếng Anh." },
                { "id": f"l{day}_2", "sentence": "This is a good day.", "sentenceVi": "Hôm nay là một ngày tốt." }
            ],
            "speaking": [
                { "id": f"s{day}_1", "sentence": "How are you today?", "sentenceVi": "Hôm nay bạn thế nào?" }
            ],
            "writing": [
                {
                    "id": f"w{day}_1",
                    "type": "fill-blank",
                    "instruction": "Điền vào chỗ trống",
                    "question": "I like studying _____.",
                    "answer": "English",
                    "hint": "Ngôn ngữ bạn đang học"
                }
            ],
            "quizzes": [
                {
                    "id": f"q{day}_1",
                    "question": f"Từ vựng 'Word_{day}_1' nghĩa là gì?",
                    "options": ["Từ vựng mẫu 1", "Từ vựng mẫu 2", "Từ vựng mẫu 3", "Từ vựng mẫu 4"],
                    "correct": 0
                }
            ],
            "conversation": [
                { "speaker": "A", "text": "Hello, how are you?", "textVi": "Xin chào, bạn khỏe không?" },
                { "speaker": "B", "text": "I am fine, thank you.", "textVi": "Tôi khỏe, cảm ơn bạn." }
            ]
        }

        # Add Day 1 specific details to match existing requirements
        if day == 1:
            lesson_data["vocabulary"] = [
              {"id": "v1", "word": "Hello", "phonetic": "/həˈloʊ/", "meaning": "Xin chào", "example": "Hello, how are you?", "exampleVi": "Xin chào, bạn khỏe không?"},
              {"id": "v2", "word": "Goodbye", "phonetic": "/ɡʊdˈbaɪ/", "meaning": "Tạm biệt", "example": "Goodbye, see you tomorrow!", "exampleVi": "Tạm biệt, hẹn gặp lại ngày mai!"}
            ]
            lesson_data["quizzes"] = [
                {"id": "q1", "question": '"Hello" nghĩa là gì?', "options": ["Xin chào", "Tạm biệt", "Cảm ơn", "Xin lỗi"], "correct": 0}
            ]

        with open(os.path.join(lessons_dir, file_name), 'w', encoding='utf-8') as f:
            json.dump(lesson_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(data_dir, "lessons-index.json"), 'w', encoding='utf-8') as f:
    json.dump(lessons_index, f, ensure_ascii=False, indent=2)

print("Generated lessons successfully.")
