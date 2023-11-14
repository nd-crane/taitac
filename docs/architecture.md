# Architecture Overview

### 1. Knowledge Graph (KG) Storage

#### Storage Layer
- Purpose: Store RDF triples/quads, which form the backbone of our knowledge representation.
- Technology: A specialized database optimized for RDF storage ensuring speed, scalability, and efficient querying.

#### SPARQL Endpoint
- Purpose: Provide an interface for querying the KG.
- Technology: A standard SPARQL endpoint ensuring compatibility with various tools and services.

### 2. Microservices Layer

#### SPARQL Service
- Purpose: Interface with the KG to fetch relevant data.
- Features:
  - Fetch data using SPARQL queries.
  - Convert query results, primarily to JSON-LD format for interoperability.

#### OpenAPI Service
- Purpose: Expose data and functionalities as RESTful services.
- Features:
  - Standard REST API endpoint allowing CRUD operations.
  - Integration points for third-party services and applications.

#### LLM Cognitive Agent Service
- Purpose: Provide intelligent, natural language processing capabilities.
- Features:
  - Process and understand natural language queries.
  - Interact with SPARQL and OpenAPI services.
  - Return comprehensive, human-friendly responses.
  - Learn and refine its knowledge based on continuous feedback.

### 3. Integration Middleware

#### JSON-LD Processor
- Purpose: Ensure semantic interoperability.
- Features:
  - Convert data between JSON-LD and other formats.
  - Support semantic annotations and context-aware data transformations.

#### Translator
- Purpose: Convert user queries into actionable data requests.
- Features:
  - Translate natural language queries into SPARQL or OpenAPI requests.
  - Employ contextual understanding to optimize data retrieval strategies.

### User Interface (UI)

#### Web UI
- Purpose: Offer users an interactive platform to engage with the system.
- Features:
  - Send natural language queries.
  - Visualize KG data.
  - Receive and review responses from the LLM.

#### REST API Client
- Purpose: Programmable interface for developer interactions.
- Features:
  - Access to all underlying services for third-party integrations.
  - Build atop the platform for custom applications and utilities.

### 5. Feedback Mechanism

- Purpose: Continuously refine the LLM's knowledge and accuracy.
- Features:
  - Users can provide feedback on LLM responses.
  - The feedback loop informs the learning process of the LLM Cognitive Agent Service.

### 6. Security and Authentication

- Purpose: Ensure safe and authorized access to data and services.
- Features:
  - Secure the OpenAPI and SPARQL endpoints.
  - Implement strategies like rate limiting, API keys, or OAuth mechanisms.

### 7. Scalability and Load Balancing

- Purpose: Handle large volumes of data and high concurrency gracefully.
- Features:
  - Distribute incoming traffic with load balancers.
  - Scale storage solutions based on data growth and query demands.

### 8. Logging and Monitoring

- Purpose: Maintain system health, track interactions, and optimize performance.
- Features:
  - Monitor service health and performance metrics.
  - Log interactions, errors, and anomalies for audit and continuous improvement.

---

The proposed architecture ensures that users can fluidly interact with a vast repository of knowledge using natural language. By converting complex queries into actionable data points and leveraging the cognitive prowess of LLMs, the system is designed to deliver accurate, concise, and human-readable responses. In essence, it's a forward-looking blueprint that envisions a seamless blend of structured KGs with the intuitive cognition of LLMs, underpinned by robust, scalable, and secure services.

## Agent Architecture

### Initial Experiment Architecture from AVIS.

[AVIS: Autonomous Visual Information Seeking with Large Language Model Agent](https://arxiv.org/abs/2306.08129) is a novel framework for visual question answering that requires external knowledge. It consists of three components: a planner, a reasoner, and a working memory. The planner decides which tool to use next, such as web search, image search, or computer vision. The reasoner analyzes the output of the tool and extracts relevant information. The working memory stores the acquired information and updates it as the process progresses. AVIS uses a large language model to power both the planner and the reasoner, and leverages user behavior data to guide its decision-making.

The tool use component of AVIS is responsible for selecting the most appropriate external tool to obtain information from, based on the current state and the question. AVIS supports three types of tools: web search, image search, and computer vision. Web search queries a search engine with keywords extracted from the question and returns a list of web pages. Image search queries an image search engine with the image provided by the user and returns a list of similar images. Computer vision applies a pre-trained object detection model to the image and returns a list of detected objects and their locations.

The state graph component of AVIS is responsible for defining the possible states and transitions of the information seeking process. A state is a representation of the current knowledge acquired by AVIS, such as the question, the image, the tool outputs, and the working memory. A transition is a change of state triggered by an action, such as invoking a tool or updating the working memory. The state graph is constructed by analyzing the user behavior data collected in a user study, where human participants were asked to answer visual questions that require external knowledge using various tools. The state graph serves as a constraint for the planner to choose valid actions at each state.

A summary of the Architecture is available from the Google Research Blog [Autonomous visual information seeking with large language models](https://blog.research.google/2023/08/autonomous-visual-information-seeking.html).


![AVIS Architecture](images/AVIS_arch.png)
