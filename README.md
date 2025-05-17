# 🛠️ PSFree Lapse Toolkit - Advanced Gadget Automation

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

<p align="center">
  <img src="psfree_lapse_toolkit_logo" alt="PSFree Lapse Toolkit Logo" width="500"/>
</p>

> This toolkit is a sophisticated suite of tools designed to streamline and automate critical aspects of exploit development, particularly focusing on the generation and management of ROP/JOP gadget maps for projects like PSFree Lapse. My vision for this project is to provide a robust, extensible, and highly efficient framework that empowers developers by abstracting away the tedious and error-prone tasks, allowing them to focus on the core logic and innovation of their exploits.

> تعكس بنية هذه المجموعة التزامًا بالوضوح، والنمطية، والهندسة الاحترافية. تم تصميم كل مكون لتحقيق الأداء الأمثل وسهولة التكامل، مما يضمن أن يتمكن مطورو الاستغلالات المتمرسون وكذلك الجدد في هذا المجال من الاستفادة من قدراته بفعالية.

## 📋 Table of Contents
- [Core Philosophy & Design Principles](#core-philosophy--design-principles)
- [Key Features](#key-features)
- [Repository Structure](#repository-structure)
- [Getting Started / Usage](#getting-started--usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Core Philosophy & Design Principles

1. **Automation Excellence**: To automate every feasible step in the gadget discovery, parsing, and map generation workflow, minimizing manual intervention and maximizing accuracy.
2. **Modularity and Extensibility**: The toolkit is structured with distinct modules for different functionalities (e.g., ROPgadget output parsing, text-based gadget input). This design allows for easy maintenance, upgrades, and the addition of new tools or parsers for other gadget-finding utilities in the future.
3. **Clarity and Organization**: A meticulously organized repository structure ensures that all components—tools, examples, documentation—are easily discoverable and understandable. This promotes efficient collaboration and onboarding for new contributors.
4. **Developer-Centric Approach**: The tools are designed to be intuitive and integrate seamlessly into existing development workflows, providing clear outputs that are directly usable in target projects.

---

## الفلسفة الأساسية ومبادئ التصميم

١. **التميز في الأتمتة**: أتمتة كل خطوة ممكنة في سير عمل اكتشاف الأدوات، تحليلها، وإنشاء الخرائط، لتقليل التدخل اليدوي وزيادة الدقة إلى أقصى حد.
٢. **النمطية وقابلية التوسع**: تم بناء مجموعة الأدوات بوحدات مميزة لوظائف مختلفة (مثل تحليل مخرجات ROPgadget، وإدخال الأدوات المستند إلى النصوص). يسمح هذا التصميم بسهولة الصيانة، والترقيات، وإضافة أدوات جديدة أو محللات لأدوات أخرى للعثور على الأدوات في المستقبل.
٣. **الوضوح والتنظيم**: يضمن هيكل المستودع المنظم بدقة سهولة اكتشاف وفهم جميع المكونات - الأدوات، الأمثلة، والتوثيق. وهذا يعزز التعاون الفعال ودمج المساهمين الجدد.
٤. **نهج يركز على المطور**: تم تصميم الأدوات لتكون بديهية وتتكامل بسلاسة مع سير عمل التطوير الحالي، مع توفير مخرجات واضحة قابلة للاستخدام مباشرة في المشاريع المستهدفة.

## ✨ Key Features

* **Automated ROPgadget Output Parsing**: Includes a Python script (`tools/rop_gadget_parser/ropgadget_to_js_parser.py`) that intelligently parses the textual output of the ROPgadget tool and converts it into a JavaScript `Map` object suitable for PSFree Lapse.
* **Text-Based Gadget Map Generation**: Provides a Python script (`tools/text_gadget_parser/gadget_map_generator.py`) for generating JavaScript `Map` objects from a simple text file input, where each line defines a gadget and its offset. This is useful for manually curated gadget lists or for integrating with other tools that produce a similar format.
* **Organized Example Suite**: A comprehensive `examples/` directory showcases usage with a sample C binary, ROPgadget output, and generated JavaScript maps.
* **Extensive Documentation**: Clear documentation, including this README and detailed workflow explanations (found in `docs/`), to guide users and developers.

---

## الميزات الرئيسية

* **تحليل آلي لمخرجات ROPgadget**: يتضمن سكربت بايثون (`tools/rop_gadget_parser/ropgadget_to_js_parser.py`) يقوم بتحليل المخرجات النصية لأداة ROPgadget بذكاء وتحويلها إلى كائن `Map` بلغة JavaScript مناسب لمشروع PSFree Lapse.
* **إنشاء خرائط الأدوات من نصوص**: يوفر سكربت بايثون (`tools/text_gadget_parser/gadget_map_generator.py`) لإنشاء كائنات `Map` بلغة JavaScript من ملف نصي بسيط، حيث يحدد كل سطر أداة وإزاحتها. هذا مفيد لقوائم الأدوات المنسقة يدويًا أو للتكامل مع أدوات أخرى تنتج تنسيقًا مشابهًا.
* **مجموعة أمثلة منظمة**: يعرض مجلد `examples/` الشامل أمثلة للاستخدام مع ملف ثنائي C نموذجي، ومخرجات ROPgadget، وخرائط JavaScript التي تم إنشاؤها.
* **توثيق شامل**: وثائق واضحة، بما في ذلك ملف README هذا وشروحات مفصلة لسير العمل (موجودة في `docs/`)، لتوجيه المستخدمين والمطورين.

## 📂 Repository Structure

The repository is organized as follows to ensure clarity and ease of navigation:

<details>
<summary>View complete repository structure</summary>

```
psfree-lapse-toolkit/
├── .github/                     # Optional: For GitHub-specific files (workflows, templates)
├── tools/                       # Core developed scripts and tools
│   ├── rop_gadget_parser/       # Module for parsing ROPgadget output
│   └── text_gadget_parser/      # Module for parsing text-based gadget input
├── examples/                    # Usage examples and test files
│   ├── simple_c_testcase/       # Sample C binary and source
│   ├── sample_ropgadget_output/ # Sample ROPgadget output file
│   ├── sample_text_input/       # Sample text input for gadget_map_generator.py
│   └── generated_js_maps/       # Examples of generated JavaScript maps
├── docs/                        # Documentation files
├── .gitignore                   # Specifies intentionally untracked files that Git should ignore
└── LICENSE                      # Project's license information
```
</details>

---

## هيكل المستودع

تم تنظيم المستودع على النحو التالي لضمان الوضوح وسهولة التصفح:

<details>
<summary>عرض هيكل المستودع الكامل</summary>

```
psfree-lapse-toolkit/
├── .github/                     # اختياري: لملفات GitHub (سير العمل، القوالب)
├── tools/                       # السكربتات والأدوات الأساسية المطورة
│   ├── rop_gadget_parser/       # وحدة تحليل مخرجات ROPgadget
│   └── text_gadget_parser/      # وحدة تحليل مدخلات الأدوات المستندة إلى النصوص
├── examples/                    # أمثلة الاستخدام وملفات الاختبار
│   ├── simple_c_testcase/       # مصدر C نموذجي وملف ثنائي
│   ├── sample_ropgadget_output/ # ملف مخرجات ROPgadget نموذجي
│   ├── sample_text_input/       # مدخل نصي نموذجي لـ gadget_map_generator.py
│   └── generated_js_maps/       # أمثلة لخرائط JavaScript التي تم إنشاؤها
├── docs/                        # ملفات التوثيق
├── .gitignore                   # يحدد الملفات التي يجب أن يتجاهلها Git عمداً
└── LICENSE                      # معلومات ترخيص المشروع
```
</details>

## 🚀 Getting Started / Usage

### Prerequisites

- Python 3.x
- ROPgadget: Install via `pip install ROPgadget`
- GCC (or any C compiler) if you wish to compile the C example (`examples/simple_c_testcase/test_rop.c`).

### 1. Using the ROPgadget Output Parser

This tool converts the output of `ROPgadget` into a JavaScript `Map`.

#### Steps:

1. **Generate ROPgadget Output**: Run ROPgadget on your target binary and save its output to a file.
   ```bash
   ROPgadget --binary /path/to/your/binary > rop_output.txt
   ```

2. **Run the Parser Script**:
   ```bash
   python tools/rop_gadget_parser/ropgadget_to_js_parser.py /path/to/rop_output.txt > generated_map.js
   ```
   * Replace `/path/to/rop_output.txt` with the path to your ROPgadget output file.
   * The script will print the JavaScript `Map` code to standard output. You can redirect it to a `.js` file as shown.

   * You can also specify a custom map variable name: 
     ```bash
     python tools/rop_gadget_parser/ropgadget_to_js_parser.py your_rop_output.txt your_map_name
     ```

### 2. Using the Text-Based Gadget Map Generator

This tool generates a JavaScript `Map` from a simple text file where each line is `"gadget_string" : offset`.

#### Steps:

1. **Prepare your Gadget Text File**: Create a text file (e.g., `my_gadgets.txt`) with content like:
   ```
   "pop rax; ret" : 0x123456
   "mov rdi, rax; ret" : 0xabcdef
   ```
   (See `examples/sample_text_input/sample_gadgets.txt` for an example.)

2. **Run the Generator Script**:
   ```bash
   python tools/text_gadget_parser/gadget_map_generator.py /path/to/my_gadgets.txt > generated_map_from_text.js
   ```
   * Replace `/path/to/my_gadgets.txt` with the path to your gadget definition file.
   * The script will print the JavaScript `Map` code to standard output.

   * You can also specify a custom map variable name:
     ```bash
     python tools/text_gadget_parser/gadget_map_generator.py your_gadgets.txt your_map_name
     ```

---

## البدء / الاستخدام

### المتطلبات الأساسية

- Python 3.x
- ROPgadget: قم بالتثبيت عبر `pip install ROPgadget`
- GCC (أو أي مترجم C) إذا كنت ترغب في ترجمة مثال C (`examples/simple_c_testcase/test_rop.c`).

### ١. استخدام محلل مخرجات ROPgadget

تقوم هذه الأداة بتحويل مخرجات `ROPgadget` إلى كائن `Map` بلغة JavaScript.

#### الخطوات:

1. **إنشاء مخرجات ROPgadget**: قم بتشغيل ROPgadget على الملف الثنائي المستهدف واحفظ مخرجاته في ملف.
   ```bash
   ROPgadget --binary /path/to/your/binary > rop_output.txt
   ```

2. **تشغيل سكريبت المحلل**:
   ```bash
   python tools/rop_gadget_parser/ropgadget_to_js_parser.py /path/to/rop_output.txt > generated_map.js
   ```
   * استبدل `/path/to/rop_output.txt` بمسار ملف مخرجات ROPgadget الخاص بك.
   * سيقوم السكريبت بطباعة كود JavaScript `Map` إلى الإخراج القياسي. يمكنك إعادة توجيهه إلى ملف `.js` كما هو موضح.

   * يمكنك أيضًا تحديد اسم متغير خريطة مخصص:
     ```bash
     python tools/rop_gadget_parser/ropgadget_to_js_parser.py your_rop_output.txt your_map_name
     ```

### ٢. استخدام منشئ خرائط الأدوات المستند إلى النصوص

تنشئ هذه الأداة كائن `Map` بلغة JavaScript من ملف نصي بسيط حيث يكون كل سطر بالصيغة `"gadget_string" : offset`.

#### الخطوات:

1. **إعداد ملف الأدوات النصي**: قم بإنشاء ملف نصي (على سبيل المثال، `my_gadgets.txt`) بمحتوى مثل:
   ```
   "pop rax; ret" : 0x123456
   "mov rdi, rax; ret" : 0xabcdef
   ```
   (انظر `examples/sample_text_input/sample_gadgets.txt` للحصول على مثال).

2. **تشغيل سكريبت المنشئ**:
   ```bash
   python tools/text_gadget_parser/gadget_map_generator.py /path/to/my_gadgets.txt > generated_map_from_text.js
   ```
   * استبدل `/path/to/my_gadgets.txt` بمسار ملف تعريف الأدوات الخاص بك.
   * سيقوم السكريبت بطباعة كود JavaScript `Map` إلى الإخراج القياسي.

   * يمكنك أيضًا تحديد اسم متغير خريطة مخصص:
     ```bash
     python tools/text_gadget_parser/gadget_map_generator.py your_gadgets.txt your_map_name
     ```

## 📚 Examples

Refer to the `examples/` directory for concrete examples of input files, ROPgadget outputs, and the JavaScript maps generated by the tools in this toolkit.

---

## الأمثلة

راجع مجلد `examples/` للحصول على أمثلة ملموسة لملفات الإدخال، ومخرجات ROPgadget، وخرائط JavaScript التي تم إنشاؤها بواسطة الأدوات في هذه المجموعة.

## 👥 Contributing

Contributions that enhance the capabilities, improve performance, or expand the scope of this toolkit are highly welcome. Please feel free to fork the repository, make your changes, and submit a pull request. For major changes, it is advisable to open an issue first to discuss your proposed ideas.

---

## المساهمة

نرحب بشدة بالمساهمات التي تعزز قدرات هذه المجموعة من الأدوات، أو تحسن أداءها، أو توسع نطاقها. لا تتردد في عمل نسخة (fork) من المستودع، وإجراء التغييرات الخاصة بك، ثم إرسال طلب سحب (pull request). بالنسبة للتغييرات الكبيرة، ننصح بفتح "مشكلة" (issue) أولاً لمناقشة الأفكار المقترحة.

## 📄 License

MIT
