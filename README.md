# Agents API

A FastAPI-based application for building and managing AI agents with PostgreSQL database integration.

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- Docker and Docker Compose (for containerized deployment)
- PostgreSQL (if running locally)

### Step-by-Step Initialization

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd agents
```

#### 2. Create Environment Variables

Create a `.env` file in the root directory by copying the example:

```bash
cp env.example .env
```

Edit the `.env` file and add your configuration values:

```env
# Postgres
POSTGRES_USER="your_postgres_user"
POSTGRES_PASSWORD="your_secure_password"
POSTGRES_URL="postgresql://your_postgres_user:your_secure_password@localhost:5432/agents_db"

# API KEYS
OPENAI_API_KEY="your_openai_api_key"
PINECONE_API_KEY="your_pinecone_api_key"
SERAPI_API_KEY="your_serapi_api_key"
```

**Important:** Replace the placeholder values with your actual API keys and database credentials.

#### 3. Choose Your Execution Method

##### Option A: Run with Docker (Recommended)

```bash
docker compose up
```

This will:

- Start a PostgreSQL database container
- Build and run the FastAPI application
- Make the API available at `http://localhost:8080`

##### Option B: Run Locally

1. **Install Dependencies**

   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -r requirements.txt
   ```

2. **Start the Application**

   ```bash
   fastapi dev app/main.py
   ```

   This will start the development server at `http://localhost:8000`

#### 4. Verify Installation

- **Docker**: Visit `http://localhost:8080/docs` for the API documentation
- **Local**: Visit `http://localhost:8000/docs` for the API documentation

## 📁 Project Structure

```
agents/
├── app/
│   ├── api/
│   │   └── routes/         # API route definitions
│   ├── core/               # Core configuration
│   ├── models/             # SQLModel database models
│   ├── migrations/         # Database migrations
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Business logic services
│   └── utils/              # Utility functions
├── test/                   # Test files
├── docker-compose.yaml     # Docker configuration
├── pyproject.toml          # Project dependencies
└── .env                    # Environment variables
```

## 🛠️ Development

### Running Tests

```bash
# Using uv
uv run pytest

# Using pip
pytest
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head
```

### Code Formatting

```bash
# Format code
ruff format .

# Lint code
ruff check .
```

## 🔧 Configuration

### Environment Variables

| Variable            | Description                         | Required |
| ------------------- | ----------------------------------- | -------- |
| `POSTGRES_USER`     | PostgreSQL username                 | Yes      |
| `POSTGRES_PASSWORD` | PostgreSQL password                 | Yes      |
| `POSTGRES_URL`      | PostgreSQL connection URL           | Yes      |
| `OPENAI_API_KEY`    | OpenAI API key for AI features      | Yes      |
| `PINECONE_API_KEY`  | Pinecone API key for vector storage | Yes      |
| `SERAPI_API_KEY`    | SerAPI key for search functionality | Yes      |

## 📚 API Documentation

Once the application is running, you can access:

- **Interactive API Docs**: `/docs` (Swagger UI)
- **Alternative API Docs**: `/redoc` (ReDoc)
- **OpenAPI Schema**: `/openapi.json`

## 🐳 Docker Commands

```bash
# Start services
docker compose up

# Start services in background
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f

# Rebuild and start
docker compose up --build
```

## 🚨 Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `docker-compose.yaml` or stop conflicting services
2. **Database connection failed**: Ensure PostgreSQL is running and credentials are correct
3. **API keys not working**: Verify all API keys are valid and have sufficient credits

### Getting Help

- Check the logs: `docker compose logs -f`
- Verify environment variables are set correctly
- Ensure all prerequisites are installed

### Licence

This project is licensed under the MIT License. See the [LICENSE](LICENCE) file for details.
