# Voice Agent Order Management System

A full-stack application for managing orders with voice agent integration, built with Flask (Backend) and React + TypeScript (Frontend).

## Project Structure

```
voice-agent/
├── api.py          # Backend API implementation
├── db.py           # Database interface
├── frontend/       # React + TypeScript frontend
│   ├── src/        # Frontend source code
│   ├── public/     # Static assets
│   └── package.json
└── ReadMe.md       # Project documentation
```

## Backend API

### Features

- Get order details by order number
- Create new orders with automatic order number generation
- Comprehensive error handling and logging
- Type-safe implementations with Python type hints

### API Endpoints

#### Get Order Details

```
GET /orders

Request Body:
{
    "orderNumber": "ORD-0001"
}

Response (200 OK):
{
    "order_number": "ORD-0001",
    "customer_name": "John Doe",
    "order_date": "2024-02-20T10:30:00",
    "total_amount": 99.99,
    "status": "pending",
    "shipping_address": "123 Main St"
}
```

#### Create New Order

```
POST /orders

Request Body:
{
    "customer_name": "John Doe",
    "total_amount": 99.99,
    "shipping_address": "123 Main St"
}
```

### Backend Setup

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Flask server:

```bash
python api.py
```

The server will start on `http://0.0.0.0:5000`

## Frontend

### Features

- Modern React with TypeScript
- Vite for fast development and building
- ESLint configuration for code quality
- Hot Module Replacement (HMR)

### Frontend Setup

1. Navigate to frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start development server:

```bash
npm run dev
```

The frontend will start on `http://localhost:5173`

### Building for Production

```bash
cd frontend
npm run build
```

## Development

### Backend Dependencies

- Flask: Web framework
- Python 3.7+
- Additional requirements in requirements.txt

### Frontend Dependencies

- React 18+
- TypeScript
- Vite
- ESLint

## Logging

The application includes comprehensive logging:

- Info level for successful operations
- Error level for failures
- Logs include timestamps and relevant order information

## Future Improvements

- Add authentication and authorization
- Implement order status updates
- Add order history tracking
- Integrate with a proper database
- Add unit tests
- Add API documentation using Swagger/OpenAPI
- Implement real-time updates
- Add voice recognition features

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
