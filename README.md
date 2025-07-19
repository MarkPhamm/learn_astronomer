# Learn Astronomer 🚀

A comprehensive learning repository for **Apache Airflow** using **Astronomer** - the modern platform for building and deploying data workflows.

## Table of Contents

- [About This Project](#about-this-project)
- [What is Astronomer?](#what-is-astronomer)
- [Key Concepts](#key-concepts)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Understanding the Example DAG](#understanding-the-example-dag)
- [Learning Resources](#learning-resources)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Key Airflow Concepts](#key-airflow-concepts)
- [Astronomer Features](#astronomer-features)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)

## About This Project

This repository serves as a hands-on learning environment for mastering Apache Airflow through Astronomer. It contains practical examples, documentation, and resources to help you understand workflow orchestration, data pipelines, and modern data engineering practices.

## What is Astronomer?

**Astronomer** is the modern data orchestration platform built on Apache Airflow. It provides:

- **Managed Airflow Services**: Fully managed Apache Airflow in the cloud
- **Local Development**: Astronomer CLI for local development and testing
- **Enhanced UI**: Improved user interface and monitoring capabilities
- **Enterprise Features**: Advanced security, observability, and governance
- **Simplified Deployment**: Easy deployment and scaling of Airflow instances

### Why Astronomer?

- 🛠️ **Developer Experience**: Streamlined local development with `astro dev`
- 🚀 **Production Ready**: Enterprise-grade reliability and security
- 📊 **Observability**: Advanced monitoring and alerting capabilities
- 🔄 **CI/CD Integration**: Seamless integration with modern development workflows
- 🏢 **Enterprise Support**: Professional support and SLA guarantees

## Key Concepts

### Apache Airflow Fundamentals

- **DAG (Directed Acyclic Graph)**: A workflow definition with tasks and dependencies
- **Task**: A single unit of work (e.g., data extraction, transformation, loading)
- **Operator**: Template for a specific type of task (PythonOperator, BashOperator, etc.)
- **TaskFlow API**: Modern Python-native way to define tasks using decorators
- **XCom**: Cross-communication between tasks for passing small amounts of data
- **Dynamic Task Mapping**: Create variable numbers of tasks at runtime

### Astronomer Concepts

- **Astro Runtime**: Astronomer's distribution of Apache Airflow with additional features
- **Astro CLI**: Command-line tool for local development and deployment
- **Deployments**: Isolated Airflow environments (dev, staging, production)
- **Workspaces**: Organizational units that contain multiple deployments

## Project Structure

```
learn_astronomer/
├── astro-project/              # Main Astronomer project
│   ├── dags/                   # DAG definitions
│   │   └── example_astronauts.py  # Example ETL pipeline
│   ├── include/                # Additional files and utilities
│   ├── plugins/                # Custom Airflow plugins
│   ├── tests/                  # Test files
│   │   └── dags/
│   │       └── test_dag_integrity.py  # DAG validation tests
│   ├── Dockerfile             # Custom Docker image configuration
│   ├── packages.txt           # OS-level packages
│   ├── requirements.txt       # Python dependencies
│   └── README.md             # Astronomer project documentation
├── materials/                 # Learning materials
│   └── airflow-101.pdf       # Educational resources
└── README.md                 # This file
```

### Key Files Explained

- **`dags/`**: Contains your workflow definitions (DAGs)
- **`include/`**: Store helper functions, SQL files, or other assets
- **`plugins/`**: Custom operators, hooks, or sensors
- **`tests/`**: Unit tests and DAG validation tests
- **`Dockerfile`**: Extends the base Astro Runtime image
- **`requirements.txt`**: Python package dependencies
- **`packages.txt`**: System-level packages (apt packages)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker Desktop**: For containerized local development
- **Python 3.8+**: Required for Airflow
- **Astronomer CLI**: For managing Astro projects

## Quick Start

### 1. Install Astronomer CLI

```bash
# macOS (using Homebrew)
brew install astro

# Windows/Linux
curl -sSL install.astronomer.io | sudo bash -s
```

### 2. Verify Installation

```bash
astro version
```

### 3. Navigate to the Astro Project

```bash
cd astro-project
```

### 4. Start Local Airflow Environment

```bash
astro dev start
```

This command will:
- Build a Docker image with your DAGs and dependencies
- Start 4 containers: Webserver, Scheduler, Triggerer, and Postgres
- Make Airflow UI available at `http://localhost:8080`

### 5. Access the Airflow UI

- **URL**: `http://localhost:8080`
- **Username**: `admin`
- **Password**: `admin`

### 6. Stop the Environment

```bash
astro dev stop
```

## Understanding the Example DAG

The included `example_astronauts.py` demonstrates key Airflow concepts:

### TaskFlow API Usage

```python
@dag(
    start_date=datetime(2025, 4, 1),
    schedule="@daily",
    tags=["example", "space"]
)
def example_astronauts():
    
    @task
    def get_astronauts() -> list[dict]:
        # Fetch data from API
        pass
    
    @task
    def print_astronaut_craft(person_in_space: dict):
        # Process each astronaut
        pass
```

### Key Features Demonstrated

1. **API Integration**: Fetches real-time data from Open Notify API
2. **Dynamic Task Mapping**: Creates tasks dynamically based on data
3. **XCom Usage**: Passes data between tasks
4. **Error Handling**: Graceful fallback when API is unavailable
5. **TaskFlow API**: Modern Python-native task definition
6. **Assets/Datasets**: Defines data dependencies for downstream DAGs

## Learning Resources

### Included Materials

- **`materials/airflow-101.pdf`**: Comprehensive Airflow fundamentals guide

### Official Documentation

- [Astronomer Documentation](https://docs.astronomer.io/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Astronomer Learn](https://docs.astronomer.io/learn/) - Tutorials and guides

### Recommended Learning Path

1. **Start Here**: Read `materials/airflow-101.pdf`
2. **Hands-on**: Run and modify the example DAG
3. **Deep Dive**: Explore TaskFlow API and operators
4. **Advanced**: Learn about sensors, hooks, and custom operators
5. **Production**: Study deployment, monitoring, and best practices

## Development Workflow

### Creating a New DAG

1. Create a new Python file in `dags/`
2. Use the TaskFlow API for new DAGs
3. Test locally with `astro dev start`
4. Validate with the included tests

### Adding Dependencies

```bash
# Python packages
echo "requests==2.28.1" >> requirements.txt

# System packages
echo "curl" >> packages.txt

# Restart environment
astro dev restart
```

### Best Practices

- **Use TaskFlow API**: Modern, Pythonic approach
- **Tag your DAGs**: Organize workflows with meaningful tags
- **Set retries**: Configure appropriate retry policies
- **Document your code**: Use docstrings and DAG documentation
- **Test thoroughly**: Write tests for your DAGs

## Testing

The project includes comprehensive testing:

### Running Tests

```bash
# Run all tests
astro dev pytest

# Run specific test
astro dev pytest tests/dags/test_dag_integrity.py
```

### Test Coverage

- **Import validation**: Ensures all DAGs import without errors
- **Tag validation**: Verifies DAGs have appropriate tags
- **Retry configuration**: Checks retry policies are set
- **Custom tests**: Add your own validation logic

## Key Airflow Concepts

### Operators

- **PythonOperator**: Execute Python functions
- **BashOperator**: Run bash commands
- **EmailOperator**: Send email notifications
- **HTTPOperator**: Make HTTP requests
- **SQLOperator**: Execute SQL queries

### Scheduling

```python
# Schedule options
schedule="@daily"          # Once per day
schedule="@hourly"         # Once per hour
schedule="0 0 * * 0"       # Weekly (cron syntax)
schedule=timedelta(hours=6) # Every 6 hours
```

### Task Dependencies

```python
# Method 1: Using >> operator
task1 >> task2 >> task3

# Method 2: Using TaskFlow API (automatic)
result = task1()
task2(result)

# Method 3: Explicit dependencies
task1.set_downstream(task2)
```

## Astronomer Features

### Local Development

- **Hot Reloading**: Changes reflected immediately
- **Environment Isolation**: Docker-based development
- **Resource Management**: Configure CPU/memory limits

### Deployment Options

- **Astronomer Cloud**: Fully managed service
- **Astronomer Enterprise**: Self-hosted enterprise solution
- **Local Development**: `astro dev` for development

### Monitoring & Observability

- **Enhanced UI**: Improved Airflow interface
- **Logging**: Centralized log aggregation
- **Metrics**: Detailed performance metrics
- **Alerting**: Configurable alerts and notifications

## Troubleshooting

### Common Issues

1. **Port Conflicts**: Change ports in `docker-compose.override.yml`
2. **Memory Issues**: Increase Docker memory allocation
3. **Import Errors**: Check Python dependencies in `requirements.txt`
4. **DAG Parse Errors**: Validate syntax and imports

### Debugging Commands

```bash
# Check container status
astro dev ps

# View logs
astro dev logs

# Access container shell
astro dev bash

# Restart environment
astro dev restart
```

### Getting Help

- [Astronomer Community Forum](https://forum.astronomer.io/)
- [Astronomer Support](https://support.astronomer.io/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/airflow)

## Next Steps

### Beginner Path

1. ✅ Complete the quick start
2. 📚 Read the included learning materials
3. 🔧 Modify the example DAG
4. 📝 Create your first simple DAG
5. 🧪 Write tests for your DAGs

### Intermediate Path

1. 🔗 Connect to external data sources
2. 🐍 Explore different operators
3. 📊 Implement data quality checks
4. 🔄 Set up CI/CD pipelines
5. 📈 Add monitoring and alerting

### Advanced Path

1. 🏗️ Build custom operators and hooks
2. 🚀 Deploy to Astronomer Cloud
3. 🔒 Implement security best practices
4. ⚡ Optimize performance and scaling
5. 🏢 Enterprise deployment strategies

---

## Contributing

Feel free to contribute to this learning repository by:

- Adding new example DAGs
- Improving documentation
- Sharing learning resources
- Reporting issues or suggestions

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Learning! 🚀✨**

For questions or support, refer to the [Astronomer documentation](https://docs.astronomer.io/) or join the [community forum](https://forum.astronomer.io/).
