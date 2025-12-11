"""
Fix unit names in JavaScript for all non-Korean languages
"""

import os
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent

# Unit name translations for JavaScript
UNIT_TRANSLATIONS = {
    'en': {
        'meter': 'Meter (m)', 'kilometer': 'Kilometer (km)', 'centimeter': 'Centimeter (cm)', 
        'millimeter': 'Millimeter (mm)', 'mile': 'Mile (mi)', 'yard': 'Yard (yd)', 
        'foot': 'Foot (ft)', 'inch': 'Inch (in)',
        'kilogram': 'Kilogram (kg)', 'gram': 'Gram (g)', 'milligram': 'Milligram (mg)',
        'ton': 'Ton (t)', 'pound': 'Pound (lb)', 'ounce': 'Ounce (oz)',
        'celsius': 'Celsius (°C)', 'fahrenheit': 'Fahrenheit (°F)', 'kelvin': 'Kelvin (K)',
        'liter': 'Liter (L)', 'milliliter': 'Milliliter (mL)', 'cubicMeter': 'Cubic Meter (m³)',
        'gallon': 'Gallon (gal)', 'quart': 'Quart (qt)', 'pint': 'Pint (pt)', 'cup': 'Cup (cup)',
        'squareMeter': 'Square Meter (m²)', 'squareKilometer': 'Square Kilometer (km²)',
        'squareCentimeter': 'Square Centimeter (cm²)', 'hectare': 'Hectare (ha)',
        'acre': 'Acre (ac)', 'squareFoot': 'Square Foot (ft²)',
        'meterPerSecond': 'Meter/Second (m/s)', 'kilometerPerHour': 'Kilometer/Hour (km/h)',
        'milePerHour': 'Mile/Hour (mph)', 'knot': 'Knot (knot)'
    },
    'ja': {
        'meter': 'メートル (m)', 'kilometer': 'キロメートル (km)', 'centimeter': 'センチメートル (cm)',
        'millimeter': 'ミリメートル (mm)', 'mile': 'マイル (mi)', 'yard': 'ヤード (yd)',
        'foot': 'フィート (ft)', 'inch': 'インチ (in)',
        'kilogram': 'キログラム (kg)', 'gram': 'グラム (g)', 'milligram': 'ミリグラム (mg)',
        'ton': 'トン (t)', 'pound': 'ポンド (lb)', 'ounce': 'オンス (oz)',
        'celsius': '摂氏 (°C)', 'fahrenheit': '華氏 (°F)', 'kelvin': 'ケルビン (K)',
        'liter': 'リットル (L)', 'milliliter': 'ミリリットル (mL)', 'cubicMeter': '立方メートル (m³)',
        'gallon': 'ガロン (gal)', 'quart': 'クォート (qt)', 'pint': 'パイント (pt)', 'cup': 'カップ (cup)',
        'squareMeter': '平方メートル (m²)', 'squareKilometer': '平方キロメートル (km²)',
        'squareCentimeter': '平方センチメートル (cm²)', 'hectare': 'ヘクタール (ha)',
        'acre': 'エーカー (ac)', 'squareFoot': '平方フィート (ft²)',
        'meterPerSecond': 'メートル/秒 (m/s)', 'kilometerPerHour': 'キロメートル/時 (km/h)',
        'milePerHour': 'マイル/時 (mph)', 'knot': 'ノット (knot)'
    },
    'hi': {
        'meter': 'मीटर (m)', 'kilometer': 'किलोमीटर (km)', 'centimeter': 'सेंटीमीटर (cm)',
        'millimeter': 'मिलीमीटर (mm)', 'mile': 'मील (mi)', 'yard': 'गज (yd)',
        'foot': 'फुट (ft)', 'inch': 'इंच (in)',
        'kilogram': 'किलोग्राम (kg)', 'gram': 'ग्राम (g)', 'milligram': 'मिलीग्राम (mg)',
        'ton': 'टन (t)', 'pound': 'पाउंड (lb)', 'ounce': 'औंस (oz)',
        'celsius': 'सेल्सियस (°C)', 'fahrenheit': 'फ़ारेनहाइट (°F)', 'kelvin': 'केल्विन (K)',
        'liter': 'लीटर (L)', 'milliliter': 'मिलीलीटर (mL)', 'cubicMeter': 'घन मीटर (m³)',
        'gallon': 'गैलन (gal)', 'quart': 'क्वार्ट (qt)', 'pint': 'पिंट (pt)', 'cup': 'कप (cup)',
        'squareMeter': 'वर्ग मीटर (m²)', 'squareKilometer': 'वर्ग किलोमीटर (km²)',
        'squareCentimeter': 'वर्ग सेंटीमीटर (cm²)', 'hectare': 'हेक्टेयर (ha)',
        'acre': 'एकड़ (ac)', 'squareFoot': 'वर्ग फुट (ft²)',
        'meterPerSecond': 'मीटर/सेकंड (m/s)', 'kilometerPerHour': 'किलोमीटर/घंटा (km/h)',
        'milePerHour': 'मील/घंटा (mph)', 'knot': 'नॉट (knot)'
    },
    'id': {
        'meter': 'Meter (m)', 'kilometer': 'Kilometer (km)', 'centimeter': 'Sentimeter (cm)',
        'millimeter': 'Milimeter (mm)', 'mile': 'Mil (mi)', 'yard': 'Yard (yd)',
        'foot': 'Kaki (ft)', 'inch': 'Inci (in)',
        'kilogram': 'Kilogram (kg)', 'gram': 'Gram (g)', 'milligram': 'Miligram (mg)',
        'ton': 'Ton (t)', 'pound': 'Pon (lb)', 'ounce': 'Ons (oz)',
        'celsius': 'Celsius (°C)', 'fahrenheit': 'Fahrenheit (°F)', 'kelvin': 'Kelvin (K)',
        'liter': 'Liter (L)', 'milliliter': 'Mililiter (mL)', 'cubicMeter': 'Meter Kubik (m³)',
        'gallon': 'Galon (gal)', 'quart': 'Quart (qt)', 'pint': 'Pint (pt)', 'cup': 'Cangkir (cup)',
        'squareMeter': 'Meter Persegi (m²)', 'squareKilometer': 'Kilometer Persegi (km²)',
        'squareCentimeter': 'Sentimeter Persegi (cm²)', 'hectare': 'Hektar (ha)',
        'acre': 'Acre (ac)', 'squareFoot': 'Kaki Persegi (ft²)',
        'meterPerSecond': 'Meter/Detik (m/s)', 'kilometerPerHour': 'Kilometer/Jam (km/h)',
        'milePerHour': 'Mil/Jam (mph)', 'knot': 'Knot (knot)'
    },
    'vi': {
        'meter': 'Mét (m)', 'kilometer': 'Kilômét (km)', 'centimeter': 'Xentimét (cm)',
        'millimeter': 'Milimét (mm)', 'mile': 'Dặm (mi)', 'yard': 'Yard (yd)',
        'foot': 'Feet (ft)', 'inch': 'Inch (in)',
        'kilogram': 'Kilôgam (kg)', 'gram': 'Gam (g)', 'milligram': 'Miligam (mg)',
        'ton': 'Tấn (t)', 'pound': 'Pound (lb)', 'ounce': 'Ounce (oz)',
        'celsius': 'Celsius (°C)', 'fahrenheit': 'Fahrenheit (°F)', 'kelvin': 'Kelvin (K)',
        'liter': 'Lít (L)', 'milliliter': 'Mililít (mL)', 'cubicMeter': 'Mét Khối (m³)',
        'gallon': 'Gallon (gal)', 'quart': 'Quart (qt)', 'pint': 'Pint (pt)', 'cup': 'Cốc (cup)',
        'squareMeter': 'Mét Vuông (m²)', 'squareKilometer': 'Kilômét Vuông (km²)',
        'squareCentimeter': 'Xentimét Vuông (cm²)', 'hectare': 'Hecta (ha)',
        'acre': 'Acre (ac)', 'squareFoot': 'Feet Vuông (ft²)',
        'meterPerSecond': 'Mét/Giây (m/s)', 'kilometerPerHour': 'Kilômét/Giờ (km/h)',
        'milePerHour': 'Dặm/Giờ (mph)', 'knot': 'Hải Lý (knot)'
    },
    'th': {
        'meter': 'เมตร (m)', 'kilometer': 'กิโลเมตร (km)', 'centimeter': 'เซนติเมตร (cm)',
        'millimeter': 'มิลลิเมตร (mm)', 'mile': 'ไมล์ (mi)', 'yard': 'หลา (yd)',
        'foot': 'ฟุต (ft)', 'inch': 'นิ้ว (in)',
        'kilogram': 'กิโลกรัม (kg)', 'gram': 'กรัม (g)', 'milligram': 'มิลลิกรัม (mg)',
        'ton': 'ตัน (t)', 'pound': 'ปอนด์ (lb)', 'ounce': 'ออนซ์ (oz)',
        'celsius': 'เซลเซียส (°C)', 'fahrenheit': 'ฟาเรนไฮต์ (°F)', 'kelvin': 'เคลวิน (K)',
        'liter': 'ลิตร (L)', 'milliliter': 'มิลลิลิตร (mL)', 'cubicMeter': 'ลูกบาศก์เมตร (m³)',
        'gallon': 'แกลลอน (gal)', 'quart': 'ควอร์ต (qt)', 'pint': 'ไพน์ (pt)', 'cup': 'ถ้วย (cup)',
        'squareMeter': 'ตารางเมตร (m²)', 'squareKilometer': 'ตารางกิโลเมตร (km²)',
        'squareCentimeter': 'ตารางเซนติเมตร (cm²)', 'hectare': 'เฮกตาร์ (ha)',
        'acre': 'เอเคอร์ (ac)', 'squareFoot': 'ตารางฟุต (ft²)',
        'meterPerSecond': 'เมตร/วินาที (m/s)', 'kilometerPerHour': 'กิโลเมตร/ชั่วโมง (km/h)',
        'milePerHour': 'ไมล์/ชั่วโมง (mph)', 'knot': 'นอต (knot)'
    },
    'de': {
        'meter': 'Meter (m)', 'kilometer': 'Kilometer (km)', 'centimeter': 'Zentimeter (cm)',
        'millimeter': 'Millimeter (mm)', 'mile': 'Meile (mi)', 'yard': 'Yard (yd)',
        'foot': 'Fuß (ft)', 'inch': 'Zoll (in)',
        'kilogram': 'Kilogramm (kg)', 'gram': 'Gramm (g)', 'milligram': 'Milligramm (mg)',
        'ton': 'Tonne (t)', 'pound': 'Pfund (lb)', 'ounce': 'Unze (oz)',
        'celsius': 'Celsius (°C)', 'fahrenheit': 'Fahrenheit (°F)', 'kelvin': 'Kelvin (K)',
        'liter': 'Liter (L)', 'milliliter': 'Milliliter (mL)', 'cubicMeter': 'Kubikmeter (m³)',
        'gallon': 'Gallone (gal)', 'quart': 'Quart (qt)', 'pint': 'Pint (pt)', 'cup': 'Tasse (cup)',
        'squareMeter': 'Quadratmeter (m²)', 'squareKilometer': 'Quadratkilometer (km²)',
        'squareCentimeter': 'Quadratzentimeter (cm²)', 'hectare': 'Hektar (ha)',
        'acre': 'Acre (ac)', 'squareFoot': 'Quadratfuß (ft²)',
        'meterPerSecond': 'Meter/Sekunde (m/s)', 'kilometerPerHour': 'Kilometer/Stunde (km/h)',
        'milePerHour': 'Meilen/Stunde (mph)', 'knot': 'Knoten (knot)'
    },
    'pt': {
        'meter': 'Metro (m)', 'kilometer': 'Quilômetro (km)', 'centimeter': 'Centímetro (cm)',
        'millimeter': 'Milímetro (mm)', 'mile': 'Milha (mi)', 'yard': 'Jarda (yd)',
        'foot': 'Pé (ft)', 'inch': 'Polegada (in)',
        'kilogram': 'Quilograma (kg)', 'gram': 'Grama (g)', 'milligram': 'Miligrama (mg)',
        'ton': 'Tonelada (t)', 'pound': 'Libra (lb)', 'ounce': 'Onça (oz)',
        'celsius': 'Celsius (°C)', 'fahrenheit': 'Fahrenheit (°F)', 'kelvin': 'Kelvin (K)',
        'liter': 'Litro (L)', 'milliliter': 'Mililitro (mL)', 'cubicMeter': 'Metro Cúbico (m³)',
        'gallon': 'Galão (gal)', 'quart': 'Quarto (qt)', 'pint': 'Pint (pt)', 'cup': 'Xícara (cup)',
        'squareMeter': 'Metro Quadrado (m²)', 'squareKilometer': 'Quilômetro Quadrado (km²)',
        'squareCentimeter': 'Centímetro Quadrado (cm²)', 'hectare': 'Hectare (ha)',
        'acre': 'Acre (ac)', 'squareFoot': 'Pé Quadrado (ft²)',
        'meterPerSecond': 'Metro/Segundo (m/s)', 'kilometerPerHour': 'Quilômetro/Hora (km/h)',
        'milePerHour': 'Milha/Hora (mph)', 'knot': 'Nó (knot)'
    }
}

# Korean unit names to replace
KOREAN_UNITS = {
    'meter': '미터 (m)', 'kilometer': '킬로미터 (km)', 'centimeter': '센티미터 (cm)',
    'millimeter': '밀리미터 (mm)', 'mile': '마일 (mi)', 'yard': '야드 (yd)',
    'foot': '피트 (ft)', 'inch': '인치 (in)',
    'kilogram': '킬로그램 (kg)', 'gram': '그램 (g)', 'milligram': '밀리그램 (mg)',
    'ton': '톤 (t)', 'pound': '파운드 (lb)', 'ounce': '온스 (oz)',
    'celsius': '섭씨 (°C)', 'fahrenheit': '화씨 (°F)', 'kelvin': '켈빈 (K)',
    'liter': '리터 (L)', 'milliliter': '밀리리터 (mL)', 'cubicMeter': '세제곱미터 (m³)',
    'gallon': '갤런 (gal)', 'quart': '쿼트 (qt)', 'pint': '파인트 (pt)', 'cup': '컵 (cup)',
    'squareMeter': '제곱미터 (m²)', 'squareKilometer': '제곱킬로미터 (km²)',
    'squareCentimeter': '제곱센티미터 (cm²)', 'hectare': '헥타르 (ha)',
    'acre': '에이커 (ac)', 'squareFoot': '제곱피트 (ft²)',
    'meterPerSecond': '미터/초 (m/s)', 'kilometerPerHour': '킬로미터/시 (km/h)',
    'milePerHour': '마일/시 (mph)', 'knot': '노트 (knot)'
}

def fix_unit_names(lang):
    """Fix unit names in unit converter for a specific language"""
    file_path = BASE_DIR / lang / 'unit-converter' / 'index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace each Korean unit name with the target language
    for unit_key, korean_name in KOREAN_UNITS.items():
        if lang in UNIT_TRANSLATIONS and unit_key in UNIT_TRANSLATIONS[lang]:
            target_name = UNIT_TRANSLATIONS[lang][unit_key]
            content = content.replace(f"name: '{korean_name}'", f"name: '{target_name}'")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed: {lang}/unit-converter/index.html")

def main():
    print("🚀 Fixing unit names in JavaScript...\n")
    
    for lang in UNIT_TRANSLATIONS.keys():
        fix_unit_names(lang)
    
    print(f"\n{'='*60}")
    print(f"✨ Complete! Fixed unit names for {len(UNIT_TRANSLATIONS)} languages")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
