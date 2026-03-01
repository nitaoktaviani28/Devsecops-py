# 📚 Library App - FastAPI + React

Aplikasi web perpustakaan sederhana dengan backend FastAPI dan frontend React + Tailwind CSS.

## 🏗️ Struktur Project

```
library-app/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Backend container
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # React component
│   │   ├── main.jsx         # Entry point
│   │   └── index.css        # Tailwind CSS
│   ├── package.json         # Node dependencies
│   ├── vite.config.js       # Vite config
│   ├── tailwind.config.js   # Tailwind config
│   ├── nginx.conf           # Nginx config
│   └── Dockerfile           # Frontend container
└── k8s/
    ├── backend.yaml         # Backend K8s manifest
    └── frontend.yaml        # Frontend K8s manifest
```

## 🚀 Backend API Endpoints

- `GET /health` - Health check
- `GET /books` - Get all books
- `GET /books/{id}` - Get book by ID

## 🎨 Frontend Features

- Modern card UI dengan Tailwind CSS
- Responsive design (mobile, tablet, desktop)
- Hover effects dan animations
- Gradient background

## 🐳 Docker Build

### Backend

```bash
cd backend
docker build -t library-backend:latest .
docker run -p 8000:8000 library-backend:latest
```

### Frontend

```bash
cd frontend
docker build -t library-frontend:latest .
docker run -p 80:80 library-frontend:latest
```

## ☸️ Deploy ke Azure AKS

### 1. Build dan Push Images

```bash
# Login ke Azure Container Registry
az acr login --name your-registry

# Tag images
docker tag library-backend:latest your-registry.azurecr.io/library-backend:latest
docker tag library-frontend:latest your-registry.azurecr.io/library-frontend:latest

# Push images
docker push your-registry.azurecr.io/library-backend:latest
docker push your-registry.azurecr.io/library-frontend:latest
```

### 2. Update Kubernetes Manifests

Edit `k8s/backend.yaml` dan `k8s/frontend.yaml`:
```yaml
image: your-registry.azurecr.io/library-backend:latest
image: your-registry.azurecr.io/library-frontend:latest
```

### 3. Deploy ke AKS

```bash
# Create namespace (jika belum ada)
kubectl create namespace app

# Deploy backend
kubectl apply -f k8s/backend.yaml

# Deploy frontend
kubectl apply -f k8s/frontend.yaml

# Check status
kubectl get pods -n app
kubectl get svc -n app
```

### 4. Access Application

```bash
# Get LoadBalancer IP
kubectl get svc library-frontend -n app

# Access via browser
http://<EXTERNAL-IP>
```

## 🧪 Local Development

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Access:
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs

## 📊 Monitoring

Backend health check:
```bash
curl http://localhost:8000/health
```

## 🔧 Configuration

### Backend Environment Variables

- `PORT` - Server port (default: 8000)

### Frontend Environment Variables

- `VITE_API_URL` - Backend API URL (default: http://localhost:8000)

## 📝 Notes

- Backend menggunakan data dummy (in-memory)
- Frontend menggunakan Vite untuk fast development
- Nginx digunakan sebagai web server untuk production
- Kubernetes manifests siap untuk Azure AKS dengan node selector

---

**Ready to deploy!** 🚀
