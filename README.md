# Vector Database Example with ChromaDB

A comprehensive example project demonstrating vector database implementation using ChromaDB, OpenAI embeddings, and RAG (Retrieval Augmented Generation) for document question-answering.

## 🚀 Features

- **Multiple Implementation Approaches**: Raw ChromaDB API and LangChain integration
- **Document Processing**: Automatic text chunking and embedding generation
- **Persistent Storage**: ChromaDB with local persistence
- **RAG Implementation**: Question-answering using retrieved context
- **OpenAI Integration**: GPT models and text embeddings (text-embedding-3-small)
- **Sample Dataset**: Tech and AI news articles from May 2023

## 📁 Project Structure

```
vector-database-example/
├── data/new_articles/          # Sample text documents (AI/tech news)
├── db/                         # Persistent vector database storage
│   ├── chroma_persistent_storage/  # Raw ChromaDB storage
│   └── chroma_db_lang_chain/      # LangChain ChromaDB storage
├── vector_db_llm_load.py      # Document loading with raw ChromaDB
├── vector_db_llm_query.py     # Querying with raw ChromaDB
├── vector_db_llm_lang_chain.py # LangChain implementation
├── vector_db_llm_lang_chain_v2.py # Enhanced LangChain version
├── chroma_emb.py              # Basic embedding example
├── chroma_persist.py          # Persistence demonstration
├── lang_test.py               # LangChain testing utilities
└── app.py                     # Application entry point
```

## 🛠️ Setup

### Prerequisites

- Python 3.11 or higher
- OpenAI API key
- UV package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vector-database-example
   ```

2. **Install dependencies**
   ```bash
   # Using UV (recommended)
   uv sync

   # Or using pip
   pip install -e .
   ```

3. **Environment setup**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎯 Usage

### Raw ChromaDB Implementation

**Load documents into the vector database:**
```bash
python vector_db_llm_load.py
```

**Query the database:**
```bash
python vector_db_llm_query.py
```

### LangChain Implementation

**Basic LangChain approach:**
```bash
python vector_db_llm_lang_chain.py
```

**Enhanced LangChain approach:**
```bash
python vector_db_llm_lang_chain_v2.py
```

### Testing and Examples

**Test LangChain integration:**
```bash
python lang_test.py
```

**Basic embedding example:**
```bash
python chroma_emb.py
```

## 📊 Implementation Details

### Data Processing Pipeline

1. **Document Loading**: Reads text files from `data/new_articles/`
2. **Text Chunking**: Splits documents into 1000-character chunks with 20-character overlap
3. **Embedding Generation**: Uses OpenAI's `text-embedding-3-small` model
4. **Vector Storage**: Stores in ChromaDB with persistence
5. **Query Processing**: Similarity search with configurable result count
6. **Response Generation**: RAG using GPT-3.5-turbo or GPT-4

### Key Components

- **ChromaDB**: Vector database for embedding storage and retrieval
- **OpenAI Embeddings**: High-quality text embeddings for semantic search
- **LangChain**: Framework for building applications with language models
- **RAG Pattern**: Retrieval Augmented Generation for context-aware responses

## 🔧 Configuration

### Embedding Models
- Default: `text-embedding-3-small`
- Customizable in each implementation file

### Chat Models
- `gpt-3.5-turbo` (default for most examples)
- `gpt-4` (used in enhanced version)
- `gpt-4o-mini` (used in some examples)

### Chunking Parameters
- **Chunk Size**: 1000 characters
- **Overlap**: 20 characters
- **Separators**: `["\n\n", "\n"]`

## 📝 Example Query

```python
question = "Tell me about the spacex starship?"
relevant_chunks = query_documents(question)
answer = generate_response(question, relevant_chunks)
print(answer.content)
```

## 🔍 Sample Dataset

The project includes 20+ tech news articles from May 2023 covering:
- AI startup investments and acquisitions
- OpenAI and ChatGPT developments
- Microsoft and Google AI initiatives
- SpaceX Starship updates
- AI regulation and policy discussions

## 🛡️ Error Handling

Common issues and solutions:

1. **Import errors for LangChain**: Install missing packages:
   ```bash
   uv add langchain-openai langchain-community
   ```

2. **API key issues**: Ensure `.env` file contains valid OpenAI API key

3. **Database persistence**: ChromaDB automatically creates database directories

## 🔗 Dependencies

- `chromadb>=1.0.15`: Vector database
- `langchain>=0.3.27`: LLM application framework
- `langchain-community>=0.3.27`: Community integrations
- `langchain-openai>=0.3.28`: OpenAI integrations
- `openai>=1.98.0`: OpenAI API client

## 📚 Learning Resources

This project demonstrates:
- Vector database fundamentals
- Embedding generation and storage
- Semantic search implementation
- RAG pattern for question-answering
- LangChain framework usage
- ChromaDB integration patterns

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for improvements.

## 📄 License

This project is open source and available under the MIT License.