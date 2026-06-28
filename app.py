import streamlit as st
import datetime

class SASP_AdvancedSystem:
    def __init__(self):
        self.abjad = {'أ':1, 'ب':2, 'ج':3, 'د':4, 'ه':5, 'و':6, 'ز':7, 'ح':8, 'ط':9, 'ي':10, 'ك':20, 'ل':30, 'م':40, 'ن':50, 'س':60, 'ع':70, 'ف':80, 'ص':90, 'ق':100, 'ر':200, 'ش':300, 'ت':400, 'ث':500, 'خ':600, 'ذ':700, 'ض':800, 'ظ':900, 'غ':1000}
        self.kings = {
            "نار": {"علوي": "رقايائيل", "سفلي": "مذهب", "كوكب": "الشمس", "بخور": "لبان ذكر"},
            "تراب": {"علوي": "كسفيائيل", "سفلي": "الأحمر", "كوكب": "زحل", "بخور": "مستكة"},
            "هواء": {"علوي": "جبرائيل", "سفلي": "الأبيض", "كوكب": "المشتري", "بخور": "عود"},
            "ماء": {"علوي": "عنقيائيل", "سفلي": "شمروش", "كوكب": "الزهرة", "بخور": "جاوى"}
        }

    def calculate_total(self, text):
        return sum(self.abjad.get(c, 0) for c in text)

    def process_work(self, student, target, work_type, date):
        total_s = self.calculate_total(student)
        total_t = self.calculate_total(target)
        final_total = total_s + total_t
        tabi = list(self.kings.keys())[final_total % 4]
        
        return {
            "العدد_المركب": final_total,
            "الطبع_الغالب": tabi,
            "الملك_العلوي": self.kings[tabi]["علوي"],
            "الملك_السفلي": self.kings[tabi]["سفلي"],
            "الكوكب_المناسب": self.kings[tabi]["كوكب"],
            "البخور_اللازم": self.kings[tabi]["بخور"],
            "التصريف": f"عمل {work_type} بين {student} و {target} في يوم {date.strftime('%A')}"
        }

# واجهة المستخدم
st.title("نظام سي عبد الله الموسوعي - SASP v2")
name = st.text_input("اسم الطالب:")
target_name = st.text_input("اسم المطلوب:")
work_type = st.selectbox("نوع العمل:", ["زواج", "فراق", "جلب رزق", "إبطال سحر"])
date = st.date_input("تاريخ العمل:")

if st.button("استخراج المخطوطة"):
    system = SASP_AdvancedSystem()
    results = system.process_work(name, target_name, work_type, date)
    
    st.write("### مخرجات المخطوطة الدقيقة:")
    for key, value in results.items():
        st.write(f"**{key}**: {value}")
    
    st.info("قم بتسجيل هذه البيانات في فهرسك الخاص لاستخدامها في وقت العمل المناسب.")
