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

week2_data = {
    10: { # Travel
        "grammar_affirmative": [{"en": "I am traveling to France.", "vi": "Tôi đang đi du lịch đến Pháp."}, {"en": "She is packing her suitcase.", "vi": "Cô ấy đang đóng gói hành lý."}, {"en": "We are staying at a hotel.", "vi": "Chúng tôi đang ở tại một khách sạn."}],
        "grammar_negative": [{"en": "He is not flying today.", "vi": "Anh ấy không bay hôm nay."}, {"en": "They are not taking a bus.", "vi": "Họ không đi xe buýt."}, {"en": "I am not going abroad.", "vi": "Tôi không đi nước ngoài."}],
        "vocabulary": [
            {"word": "Travel", "phonetic": "/ˈtræv.əl/", "meaning": "Du lịch", "example": "I love travel.", "exampleVi": "Tôi yêu du lịch."},
            {"word": "Holiday", "phonetic": "/ˈhɑː.lə.deɪ/", "meaning": "Ngày lễ/Kỳ nghỉ", "example": "A long holiday.", "exampleVi": "Một kỳ nghỉ dài."},
            {"word": "Suitcase", "phonetic": "/ˈsuːt.keɪs/", "meaning": "Vali", "example": "Pack your suitcase.", "exampleVi": "Hãy đóng gói vali của bạn."},
            {"word": "Ticket", "phonetic": "/ˈtɪk.ɪt/", "meaning": "Vé", "example": "Buy a ticket.", "exampleVi": "Mua một chiếc vé."},
            {"word": "Passport", "phonetic": "/ˈpæs.pɔːrt/", "meaning": "Hộ chiếu", "example": "Show your passport.", "exampleVi": "Cho xem hộ chiếu của bạn."},
            {"word": "Hotel", "phonetic": "/hoʊˈtel/", "meaning": "Khách sạn", "example": "Stay at a hotel.", "exampleVi": "Ở tại khách sạn."},
            {"word": "Airport", "phonetic": "/ˈer.pɔːrt/", "meaning": "Sân bay", "example": "Go to the airport.", "exampleVi": "Đi đến sân bay."},
            {"word": "Beach", "phonetic": "/biːtʃ/", "meaning": "Bãi biển", "example": "I like the beach.", "exampleVi": "Tôi thích bãi biển."},
            {"word": "Tour", "phonetic": "/tʊr/", "meaning": "Chuyến tham quan", "example": "A city tour.", "exampleVi": "Một chuyến tham quan thành phố."},
            {"word": "Flight", "phonetic": "/flaɪt/", "meaning": "Chuyến bay", "example": "The flight is late.", "exampleVi": "Chuyến bay bị trễ."}
        ],
        "listening": [{"en": "We are going on holiday next week.", "vi": "Chúng tôi sẽ đi nghỉ vào tuần tới."}, {"en": "I am looking for my passport.", "vi": "Tôi đang tìm hộ chiếu của mình."}, {"en": "She is booking a hotel room.", "vi": "Cô ấy đang đặt phòng khách sạn."}, {"en": "The airport is very crowded today.", "vi": "Sân bay hôm nay rất đông đúc."}, {"en": "Are you taking a flight to Paris?", "vi": "Bạn có đang đi chuyến bay đến Paris không?"}, {"en": "We are staying near the beach.", "vi": "Chúng tôi đang ở gần bãi biển."}, {"en": "Don't forget your suitcase!", "vi": "Đừng quên vali của bạn!"}, {"en": "They are having a great time.", "vi": "Họ đang có một khoảng thời gian tuyệt vời."}, {"en": "I am buying a train ticket.", "vi": "Tôi đang mua một chiếc vé tàu."}, {"en": "The tour starts at 9 AM.", "vi": "Chuyến tham quan bắt đầu lúc 9 giờ sáng."}],
        "speaking": [{"en": "Where are you going for your holiday?", "vi": "Bạn sẽ đi đâu vào kỳ nghỉ?"}, {"en": "I am going to Thailand.", "vi": "Tôi đang đi đến Thái Lan."}, {"en": "Are you traveling alone?", "vi": "Bạn đi du lịch một mình à?"}, {"en": "No, with my family.", "vi": "Không, cùng với gia đình."}, {"en": "What are you packing?", "vi": "Bạn đang đóng gói gì thế?"}, {"en": "Just some clothes.", "vi": "Chỉ là một ít quần áo."}, {"en": "Have a safe flight!", "vi": "Chúc một chuyến bay an toàn!"}, {"en": "Thank you very much.", "vi": "Cảm ơn bạn rất nhiều."}, {"en": "Is the hotel expensive?", "vi": "Khách sạn có đắt không?"}, {"en": "It's quite cheap.", "vi": "Nó khá rẻ."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I am _____ to Paris.", "answer": "traveling", "hint": "đang đi du lịch"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Show your _____.", "answer": "passport", "hint": "hộ chiếu"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Pack your _____.", "answer": "suitcase", "hint": "vali"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Stay at a _____.", "answer": "hotel", "hint": "khách sạn"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Go to the _____.", "answer": "airport", "hint": "sân bay"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Buy a _____.", "answer": "ticket", "hint": "vé"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A city _____.", "answer": "tour", "hint": "chuyến tham quan"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ is late.", "answer": "flight", "hint": "chuyến bay"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I love the _____.", "answer": "beach", "hint": "bãi biển"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A long _____.", "answer": "holiday", "hint": "kỳ nghỉ"}],
        "quizzes": [{"question": "'Passport' nghĩa là gì?", "options": ["Hộ chiếu", "Chứng minh thư", "Bằng lái", "Vé"], "correct": 0}, {"question": "She _____ traveling to Japan.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "They are _____ at a hotel.", "options": ["stay", "staying", "stays", "stayed"], "correct": 1}, {"question": "Are you _____ your suitcase?", "options": ["pack", "packing", "packs", "packed"], "correct": 1}, {"question": "I am _____ buying a ticket.", "options": ["not", "no", "don't", "doesn't"], "correct": 0}, {"question": "Go _____ the airport.", "options": ["to", "at", "in", "on"], "correct": 0}, {"question": "'Flight' nghĩa là gì?", "options": ["Chuyến bay", "Chuyến xe", "Chuyến tàu", "Chuyến đi"], "correct": 0}, {"question": "Where _____ they traveling?", "options": ["is", "am", "are", "do"], "correct": 2}, {"question": "We _____ having fun.", "options": ["is", "am", "are", "do"], "correct": 2}, {"question": "A _____ ticket.", "options": ["train", "training", "trains", "trained"], "correct": 0}]
    },
    11: { # Weather
        "grammar_affirmative": [{"en": "It is raining outside.", "vi": "Ngoài trời đang mưa."}, {"en": "The sun is shining.", "vi": "Mặt trời đang chiếu sáng."}, {"en": "The wind is blowing hard.", "vi": "Gió đang thổi mạnh."}],
        "grammar_negative": [{"en": "It is not snowing now.", "vi": "Bây giờ trời không có tuyết."}, {"en": "The sun is not shining today.", "vi": "Hôm nay mặt trời không chiếu sáng."}, {"en": "It isn't getting hot.", "vi": "Trời không đang trở nên nóng."}],
        "vocabulary": [
            {"word": "Weather", "phonetic": "/ˈweð.ɚ/", "meaning": "Thời tiết", "example": "Nice weather.", "exampleVi": "Thời tiết đẹp."},
            {"word": "Sun", "phonetic": "/sʌn/", "meaning": "Mặt trời", "example": "The sun is hot.", "exampleVi": "Mặt trời nóng."},
            {"word": "Rain", "phonetic": "/reɪn/", "meaning": "Mưa", "example": "I like rain.", "exampleVi": "Tôi thích mưa."},
            {"word": "Cloud", "phonetic": "/klaʊd/", "meaning": "Mây", "example": "A white cloud.", "exampleVi": "Một đám mây trắng."},
            {"word": "Snow", "phonetic": "/snoʊ/", "meaning": "Tuyết", "example": "I love snow.", "exampleVi": "Tôi yêu tuyết."},
            {"word": "Wind", "phonetic": "/wɪnd/", "meaning": "Gió", "example": "The wind is cold.", "exampleVi": "Gió lạnh."},
            {"word": "Hot", "phonetic": "/hɑːt/", "meaning": "Nóng", "example": "It is hot.", "exampleVi": "Trời nóng."},
            {"word": "Cold", "phonetic": "/koʊld/", "meaning": "Lạnh", "example": "It is cold.", "exampleVi": "Trời lạnh."},
            {"word": "Storm", "phonetic": "/stɔːrm/", "meaning": "Bão", "example": "A big storm.", "exampleVi": "Một cơn bão lớn."},
            {"word": "Sky", "phonetic": "/skaɪ/", "meaning": "Bầu trời", "example": "The sky is blue.", "exampleVi": "Bầu trời màu xanh."}
        ],
        "listening": [{"en": "What is the weather like?", "vi": "Thời tiết thế nào?"}, {"en": "It is raining very hard.", "vi": "Trời đang mưa rất to."}, {"en": "The sun is coming out now.", "vi": "Mặt trời đang ló dạng."}, {"en": "It is snowing in the mountains.", "vi": "Tuyết đang rơi trên núi."}, {"en": "The wind is blowing from the north.", "vi": "Gió đang thổi từ phía bắc."}, {"en": "There are many clouds in the sky.", "vi": "Có rất nhiều mây trên bầu trời."}, {"en": "Is it getting hot today?", "vi": "Hôm nay trời có đang trở nên nóng không?"}, {"en": "The storm is passing by.", "vi": "Cơn bão đang đi qua."}, {"en": "It is getting dark and cold.", "vi": "Trời đang trở nên tối và lạnh."}, {"en": "I love sunny weather.", "vi": "Tôi yêu thời tiết nắng ráo."}],
        "speaking": [{"en": "Is it raining?", "vi": "Trời có đang mưa không?"}, {"en": "Yes, take an umbrella.", "vi": "Có, hãy mang theo ô."}, {"en": "How is the weather today?", "vi": "Thời tiết hôm nay thế nào?"}, {"en": "It's sunny and hot.", "vi": "Trời nắng và nóng."}, {"en": "Is it snowing?", "vi": "Trời có đang rơi tuyết không?"}, {"en": "No, it's just cold.", "vi": "Không, chỉ là lạnh thôi."}, {"en": "The wind is strong.", "vi": "Gió mạnh quá."}, {"en": "The sky is very clear.", "vi": "Bầu trời rất trong xanh."}, {"en": "Look at the snow!", "vi": "Nhìn tuyết kìa!"}, {"en": "It's a beautiful day.", "vi": "Đó là một ngày đẹp trời."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "It is _____ outside.", "answer": "raining", "hint": "đang mưa"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ is shining.", "answer": "sun", "hint": "mặt trời"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ is blue.", "answer": "sky", "hint": "bầu trời"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "It is _____.", "answer": "hot", "hint": "nóng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "It is _____.", "answer": "cold", "hint": "lạnh"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A white _____.", "answer": "cloud", "hint": "đám mây"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ is blowing.", "answer": "wind", "hint": "gió"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I love _____.", "answer": "snow", "hint": "tuyết"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A big _____.", "answer": "storm", "hint": "cơn bão"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Nice _____.", "answer": "weather", "hint": "thời tiết"}],
        "quizzes": [{"question": "'Rain' nghĩa là gì?", "options": ["Nắng", "Mưa", "Gió", "Bão"], "correct": 1}, {"question": "It is _____ now.", "options": ["snowing", "snow", "snows", "snowed"], "correct": 0}, {"question": "The sun _____ shining.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "The wind is _____ hard.", "options": ["blow", "blowing", "blows", "blew"], "correct": 1}, {"question": "Is it _____ hot?", "options": ["get", "gets", "getting", "got"], "correct": 2}, {"question": "The sky _____ blue.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "'Cold' nghĩa là gì?", "options": ["Nóng", "Lạnh", "Ấm", "Mát"], "correct": 1}, {"question": "There are many _____.", "options": ["cloud", "clouds", "cloudy", "clouding"], "correct": 1}, {"question": "It _____ not raining.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "A _____ day.", "options": ["sun", "sunny", "sunshine", "sunned"], "correct": 1}]
    }
}

for d in week2_data:
    update_lesson(d, week2_data[d])
print("Week 2 Batch 2 updated.")
