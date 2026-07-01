# Eksperimen SML - Salsabila Julianti

Repository ini berisi proses eksperimen dan preprocessing dataset Adult Income sebagai bagian dari Submission Sistem Machine Learning Dicoding.

## Struktur Repository

```
Eksperimen_SML-Salsabila-Julianti/
│
├── .github/
│   └── workflows/
│       └── preprocessing.yml
│
├── preprocessing/
│   ├── Eksperimen_MSML.ipynb
│   ├── automate.py
│   └── adult_preprocessed.csv
│
├── adult.data
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

Dataset yang digunakan adalah Adult Income Dataset.

## Menjalankan Preprocessing

Install dependencies:

```bash
pip install -r requirements.txt
```

Jalankan preprocessing:

```bash
python preprocessing/automate.py
```

Dataset hasil preprocessing akan tersimpan sebagai:

```
preprocessing/adult_preprocessed.csv
```

## Workflow GitHub Actions

Workflow akan otomatis dijalankan setiap terjadi push ke branch `main`.

Tahapan workflow:
- Install dependencies
- Menjalankan preprocessing
- Menghasilkan dataset preprocessing terbaru

## Author

Salsabila Julianti