#!/bin/bash

# DSKYpoly Docker Management Script
# Easy Docker operations for Windows 11 Docker Desktop

set -e

PROJECT_NAME="dskypoly"
DOCKER_IMAGE="$PROJECT_NAME:latest"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_banner() {
    echo -e "${BLUE}"
    echo "🧮 DSKYpoly Docker Management"
    echo "============================="
    echo -e "${NC}"
}

print_usage() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  build       - Build the Docker image"
    echo "  run         - Run the main development container"
    echo "  jupyter     - Start Jupyter notebook server"
    echo "  shell       - Get a shell in the running container"
    echo "  stop        - Stop all DSKYpoly containers"
    echo "  clean       - Remove containers and images"
    echo "  status      - Show container status"
    echo "  logs        - Show container logs"
    echo "  help        - Show this help message"
    echo ""
    echo "Windows 11 Docker Desktop Integration:"
    echo "  - Containers will appear in Docker Desktop GUI"
    echo "  - Volumes are managed automatically"
    echo "  - Port forwarding configured for web interfaces"
}

build_image() {
    echo -e "${GREEN}Building DSKYpoly Docker image...${NC}"
    docker build -t $DOCKER_IMAGE .
    echo -e "${GREEN}✓ Image built successfully!${NC}"
}

run_container() {
    echo -e "${GREEN}Starting DSKYpoly development container...${NC}"
    docker-compose up -d dskypoly-dev
    echo -e "${GREEN}✓ Container started!${NC}"
    echo -e "${YELLOW}Run 'docker exec -it dskypoly-mathematical-workspace /bin/bash' to get a shell${NC}"
}

start_jupyter() {
    echo -e "${GREEN}Starting Jupyter analytics environment...${NC}"
    docker-compose up -d dskypoly-analytics
    echo -e "${GREEN}✓ Jupyter started!${NC}"
    echo -e "${YELLOW}Access at: http://localhost:8888${NC}"
}

get_shell() {
    echo -e "${GREEN}Opening shell in DSKYpoly container...${NC}"
    docker exec -it dskypoly-mathematical-workspace /bin/bash
}

stop_containers() {
    echo -e "${YELLOW}Stopping all DSKYpoly containers...${NC}"
    docker-compose down
    echo -e "${GREEN}✓ Containers stopped!${NC}"
}

clean_all() {
    echo -e "${YELLOW}Cleaning up DSKYpoly containers and images...${NC}"
    docker-compose down -v
    docker rmi $DOCKER_IMAGE 2>/dev/null || true
    docker system prune -f
    echo -e "${GREEN}✓ Cleanup complete!${NC}"
}

show_status() {
    echo -e "${BLUE}DSKYpoly Container Status:${NC}"
    docker-compose ps
    echo ""
    echo -e "${BLUE}Docker Images:${NC}"
    docker images | grep $PROJECT_NAME || echo "No DSKYpoly images found"
}

show_logs() {
    echo -e "${BLUE}DSKYpoly Container Logs:${NC}"
    docker-compose logs --tail=50 -f
}

# Main script logic
case "$1" in
    "build")
        print_banner
        build_image
        ;;
    "run")
        print_banner
        run_container
        ;;
    "jupyter")
        print_banner
        start_jupyter
        ;;
    "shell")
        print_banner
        get_shell
        ;;
    "stop")
        print_banner
        stop_containers
        ;;
    "clean")
        print_banner
        clean_all
        ;;
    "status")
        print_banner
        show_status
        ;;
    "logs")
        print_banner
        show_logs
        ;;
    "help"|"--help"|"-h")
        print_banner
        print_usage
        ;;
    *)
        print_banner
        echo -e "${RED}Error: Unknown command '$1'${NC}"
        echo ""
        print_usage
        exit 1
        ;;
esac
