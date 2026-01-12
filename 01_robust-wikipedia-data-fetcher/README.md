# Robust Wikipedia Data Fetcher

A production-ready Python project that retrieves structured data from the official Wikipedia Public API, validates responses, handles failures, and stores clean output in JSON format.

This project focuses on building a reliable and maintainable API data pipeline.

---

## 🎯 Project Objective

To design a fault-tolerant data fetcher that:

- Uses the official Wikipedia API  
- Retrieves structured article data  
- Validates responses using Pydantic   
- Handles API errors, invalid data  and network errors  
- Logs failures and retries  
- Saves clean, structured output  

This project demonstrates real-world API integration practices.

---

## 📌 Key Features

- Wikipedia API search integration  
- Schema validation using Pydantic  
- Error handling for:
  - Network issues  
  - Invalid responses  
  - Empty results  
- Retry mechanism with backoff  
- Rate limiting awareness  
- Structured logging  
- JSON-based data storage  
- Configurable search queries  
- Modular Python structure  

---

## 🧠 What Problem This Solves

Public APIs require:

- Controlled access  
- Reliable requests  
- Clean data handling  
- Error resilience  

This project ensures:

- API responses are validated  
- Failures are logged  
- Data is always structured  
- The system remains stable  

---

## ⚙️ How It Works (High Level)

1. User provides a search query  
2. Wikipedia API is called  
3. Response is validated  
4. Errors are handled  
5. Results are cleaned  
6. Data is saved to JSON  
7. Logs are generated  

---

## 🛠️ Technology Stack

- **Language:** Python  
- **HTTP Client:** requests / httpx /  aiohttp  
- **Validation:** Pydantic  
- **Logging:** logging  
- **Storage:** JSON  
- **API:** Wikipedia Public API 

---

## 📂 Project Structure
01_robust-wikipedia-data-fetcher/<br/>
├── src/<br/>
│   ├── models.py<br/>
│   ├── logger.py<br/>
│   ├── fetcher.py<br/>
│   └── main.py<br/>
├── output/<br/>
├── logs/<br/>
└── README.md<br/>


---

## 🔍 Example Use Case

A research team wants to:

1. Search Wikipedia for “Artificial Intelligence”  
2. Collect article summaries  
3. Validate the response structure  
4. Store the data for analysis  

This project automates that process reliably