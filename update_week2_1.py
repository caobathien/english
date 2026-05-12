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
    8: { # Describing People
        "grammar_affirmative": [{"en": "She is wearing a blue hat.", "vi": "Cô ấy đang đội một chiếc mũ xanh."}, {"en": "They are talking to the teacher.", "vi": "Họ đang nói chuyện với giáo viên."}, {"en": "I am looking for my friend.", "vi": "Tôi đang tìm bạn của mình."}],
        "grammar_negative": [{"en": "He is not wearing glasses.", "vi": "Anh ấy không đeo kính."}, {"en": "We are not watching the movie.", "vi": "Chúng tôi không đang xem phim."}, {"en": "She is not feeling well.", "vi": "Cô ấy cảm thấy không khỏe."}],
        "vocabulary": [
            {"word": "Tall", "phonetic": "/tɑːl/", "meaning": "Cao", "example": "He is very tall.", "exampleVi": "Anh ấy rất cao."},
            {"word": "Short", "phonetic": "/ʃɔːrt/", "meaning": "Thấp/Ngắn", "example": "She is short.", "exampleVi": "Cô ấy thấp."},
            {"word": "Beautiful", "phonetic": "/ˈbjuː.t̬ə.fəl/", "meaning": "Đẹp", "example": "A beautiful girl.", "exampleVi": "Một cô gái đẹp."},
            {"word": "Handsome", "phonetic": "/ˈhæn.səm/", "meaning": "Đẹp trai", "example": "A handsome man.", "exampleVi": "Một người đàn ông đẹp trai."},
            {"word": "Kind", "phonetic": "/kaɪnd/", "meaning": "Tốt bụng", "example": "They are kind.", "exampleVi": "Họ tốt bụng."},
            {"word": "Friendly", "phonetic": "/ˈfrend.li/", "meaning": "Thân thiện", "example": "A friendly smile.", "exampleVi": "Một nụ cười thân thiện."},
            {"word": "Old", "phonetic": "/oʊld/", "meaning": "Già/Cũ", "example": "An old man.", "exampleVi": "Một cụ già."},
            {"word": "Young", "phonetic": "/jʌŋ/", "meaning": "Trẻ", "example": "A young boy.", "exampleVi": "Một cậu bé."},
            {"word": "Thin", "phonetic": "/θɪn/", "meaning": "Gầy", "example": "He is thin.", "exampleVi": "Anh ấy gầy."},
            {"word": "Happy", "phonetic": "/ˈhæp.i/", "meaning": "Hạnh phúc", "example": "They are happy.", "exampleVi": "Họ hạnh phúc."}
        ],
        "listening": [{"en": "Who is that tall man?", "vi": "Người đàn ông cao lớn kia là ai?"}, {"en": "He is my uncle.", "vi": "Ông ấy là chú của tôi."}, {"en": "She is wearing a red dress today.", "vi": "Hôm nay cô ấy đang mặc một chiếc váy đỏ."}, {"en": "Are they looking for someone?", "vi": "Họ đang tìm ai đó phải không?"}, {"en": "The teacher is very kind to us.", "vi": "Giáo viên rất tốt bụng với chúng tôi."}, {"en": "He is a handsome actor.", "vi": "Anh ấy là một diễn viên đẹp trai."}, {"en": "My grandmother is getting old.", "vi": "Bà tôi đang già đi."}, {"en": "They are always friendly.", "vi": "Họ luôn luôn thân thiện."}, {"en": "Why is she feeling sad?", "vi": "Tại sao cô ấy lại cảm thấy buồn?"}, {"en": "He is not wearing a coat.", "vi": "Anh ấy không mặc áo khoác."}],
        "speaking": [{"en": "Describe your best friend.", "vi": "Hãy mô tả người bạn thân nhất của bạn."}, {"en": "She is tall and beautiful.", "vi": "Cô ấy cao và xinh đẹp."}, {"en": "Is he wearing a hat?", "vi": "Anh ấy có đang đội mũ không?"}, {"en": "No, he isn't.", "vi": "Không, anh ấy không."}, {"en": "They are laughing.", "vi": "Họ đang cười."}, {"en": "What are you doing?", "vi": "Bạn đang làm gì thế?"}, {"en": "I am writing a letter.", "vi": "Tôi đang viết một bức thư."}, {"en": "She is a young teacher.", "vi": "Cô ấy là một giáo viên trẻ."}, {"en": "They look very happy.", "vi": "Họ trông rất hạnh phúc."}, {"en": "He is a kind person.", "vi": "Anh ấy là một người tốt bụng."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is _____ a red hat.", "answer": "wearing", "hint": "đang đội/mặc"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is very _____.", "answer": "tall", "hint": "cao"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "They are _____.", "answer": "happy", "hint": "hạnh phúc"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A _____ girl.", "answer": "beautiful", "hint": "xinh đẹp"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A _____ man.", "answer": "handsome", "hint": "đẹp trai"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He is _____.", "answer": "thin", "hint": "gầy"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "They are _____ people.", "answer": "kind", "hint": "tốt bụng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A _____ boy.", "answer": "young", "hint": "trẻ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She is _____.", "answer": "short", "hint": "thấp"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "We are _____ the movie.", "answer": "watching", "hint": "đang xem"}],
        "quizzes": [{"question": "'Beautiful' nghĩa là gì?", "options": ["Xấu", "Đẹp", "Cao", "Thấp"], "correct": 1}, {"question": "She _____ wearing a hat.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "They _____ not laughing.", "options": ["is", "am", "are", "be"], "correct": 2}, {"question": "What _____ you doing?", "options": ["is", "am", "are", "do"], "correct": 2}, {"question": "He is a _____ man.", "options": ["handsome", "beautiful", "thinly", "happily"], "correct": 0}, {"question": "I am _____ for my key.", "options": ["look", "looking", "looks", "looked"], "correct": 1}, {"question": "'Tall' nghĩa là gì?", "options": ["Cao", "Thấp", "Gầy", "Béo"], "correct": 0}, {"question": "Are they _____?", "options": ["friendly", "friend", "friends", "friendship"], "correct": 0}, {"question": "She is _____ well.", "options": ["not feeling", "feeling not", "don't feel", "doesn't feel"], "correct": 0}, {"question": "A _____ woman.", "options": ["old", "young", "new", "thin"], "correct": 1}]
    },
    9: { # Describing Places
        "grammar_affirmative": [{"en": "The city is growing fast.", "vi": "Thành phố đang phát triển nhanh chóng."}, {"en": "They are building a new bridge.", "vi": "Họ đang xây dựng một cây cầu mới."}, {"en": "It is getting dark.", "vi": "Trời đang tối dần."}],
        "grammar_negative": [{"en": "The park is not opening today.", "vi": "Công viên không mở cửa hôm nay."}, {"en": "We are not staying in a city.", "vi": "Chúng tôi không ở trong thành phố."}, {"en": "It isn't raining now.", "vi": "Bây giờ trời không mưa."}],
        "vocabulary": [
            {"word": "City", "phonetic": "/ˈsɪt.i/", "meaning": "Thành phố", "example": "A big city.", "exampleVi": "Một thành phố lớn."},
            {"word": "Park", "phonetic": "/pɑːrk/", "meaning": "Công viên", "example": "I go to the park.", "exampleVi": "Tôi đi công viên."},
            {"word": "Bridge", "phonetic": "/brɪdʒ/", "meaning": "Cây cầu", "example": "A long bridge.", "exampleVi": "Một cây cầu dài."},
            {"word": "Mountain", "phonetic": "/ˈmaʊn.tən/", "meaning": "Núi", "example": "A high mountain.", "exampleVi": "Một ngọn núi cao."},
            {"word": "River", "phonetic": "/ˈrɪv.ɚ/", "meaning": "Con sông", "example": "A wide river.", "exampleVi": "Một con sông rộng."},
            {"word": "Building", "phonetic": "/ˈbɪl.dɪŋ/", "meaning": "Tòa nhà", "example": "A tall building.", "exampleVi": "Một tòa nhà cao tầng."},
            {"word": "Street", "phonetic": "/striːt/", "meaning": "Con phố", "example": "A busy street.", "exampleVi": "Một con phố nhộn nhịp."},
            {"word": "Village", "phonetic": "/ˈvɪl.ɪdʒ/", "meaning": "Ngôi làng", "example": "A quiet village.", "exampleVi": "Một ngôi làng yên tĩnh."},
            {"word": "Beach", "phonetic": "/biːtʃ/", "meaning": "Bãi biển", "example": "I like the beach.", "exampleVi": "Tôi thích bãi biển."},
            {"word": "Museum", "phonetic": "/mjuːˈziː.əm/", "meaning": "Bảo tàng", "example": "Visit the museum.", "exampleVi": "Tham quan bảo tàng."}
        ],
        "listening": [{"en": "This city is very modern.", "vi": "Thành phố này rất hiện đại."}, {"en": "They are planting trees in the park.", "vi": "Họ đang trồng cây trong công viên."}, {"en": "The river is flowing slowly.", "vi": "Con sông đang chảy chậm chạp."}, {"en": "Look at that tall building!", "vi": "Nhìn tòa nhà cao tầng kia kìa!"}, {"en": "The streets are very busy now.", "vi": "Các con phố hiện đang rất nhộn nhịp."}, {"en": "We are walking along the beach.", "vi": "Chúng tôi đang đi bộ dọc theo bãi biển."}, {"en": "Is the museum open today?", "vi": "Bảo tàng có mở cửa hôm nay không?"}, {"en": "They are repairing the bridge.", "vi": "Họ đang sửa chữa cây cầu."}, {"en": "The village is very quiet.", "vi": "Ngôi làng rất yên tĩnh."}, {"en": "It is getting very cold on the mountain.", "vi": "Trên núi trời đang trở nên rất lạnh."}],
        "speaking": [{"en": "Where do you live?", "vi": "Bạn sống ở đâu?"}, {"en": "I live in a small village.", "vi": "Tôi sống ở một ngôi làng nhỏ."}, {"en": "What is it like?", "vi": "Nó như thế nào?"}, {"en": "It's peaceful.", "vi": "Nó rất thanh bình."}, {"en": "Is there a river?", "vi": "Có con sông nào không?"}, {"en": "Yes, it's near my house.", "vi": "Có, nó ở gần nhà tôi."}, {"en": "They are building a mall.", "vi": "Họ đang xây một trung tâm thương mại."}, {"en": "The city is changing.", "vi": "Thành phố đang thay đổi."}, {"en": "I love the beach.", "vi": "Tôi yêu bãi biển."}, {"en": "Let's go to the park.", "vi": "Chúng ta hãy đi ra công viên nào."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The city is _____ fast.", "answer": "growing", "hint": "đang phát triển"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A tall _____.", "answer": "building", "hint": "tòa nhà"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A busy _____.", "answer": "street", "hint": "con phố"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "They are _____ a bridge.", "answer": "building", "hint": "đang xây"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I like the _____.", "answer": "beach", "hint": "bãi biển"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A quiet _____.", "answer": "village", "hint": "ngôi làng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A high _____.", "answer": "mountain", "hint": "ngọn núi"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Go to the _____.", "answer": "park", "hint": "công viên"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "A wide _____.", "answer": "river", "hint": "con sông"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Visit the _____.", "answer": "museum", "hint": "bảo tàng"}],
        "quizzes": [{"question": "'Mountain' nghĩa là gì?", "options": ["Sông", "Núi", "Biển", "Hồ"], "correct": 1}, {"question": "The city _____ changing.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "They are _____ a mall.", "options": ["build", "building", "builds", "built"], "correct": 1}, {"question": "It is _____ dark.", "options": ["get", "gets", "getting", "got"], "correct": 2}, {"question": "A _____ street.", "options": ["busy", "busily", "business", "busier"], "correct": 0}, {"question": "Are they _____ in the park?", "options": ["walk", "walking", "walks", "walked"], "correct": 1}, {"question": "'Bridge' nghĩa là gì?", "options": ["Cây cầu", "Con đường", "Tòa nhà", "Cái cổng"], "correct": 0}, {"question": "The village _____ very quiet.", "options": ["is", "am", "are", "be"], "correct": 0}, {"question": "We _____ not staying here.", "options": ["is", "am", "are", "do"], "correct": 2}, {"question": "Look _____ that building!", "options": ["at", "on", "in", "to"], "correct": 0}]
    }
}

for d in week2_data:
    update_lesson(d, week2_data[d])
print("Week 2 Batch 1 updated.")
