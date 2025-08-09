@echo off
REM DSKYpoly Docker Management for Windows 11
REM Compatible with Docker Desktop

setlocal enabledelayedexpansion

set PROJECT_NAME=dskypoly
set DOCKER_IMAGE=%PROJECT_NAME%:latest

:banner
echo.
echo 🧮 DSKYpoly Docker Management (Windows 11)
echo ========================================
echo.

if "%1"=="build" goto build
if "%1"=="run" goto run
if "%1"=="jupyter" goto jupyter
if "%1"=="shell" goto shell
if "%1"=="stop" goto stop
if "%1"=="clean" goto clean
if "%1"=="status" goto status
if "%1"=="logs" goto logs
if "%1"=="help" goto help
if "%1"=="" goto help

echo Error: Unknown command '%1'
goto help

:build
echo Building DSKYpoly Docker image...
docker build -t %DOCKER_IMAGE% .
echo ✓ Image built successfully!
goto end

:run
echo Starting DSKYpoly development container...
docker-compose up -d dskypoly-dev
echo ✓ Container started!
echo Access via: docker exec -it dskypoly-mathematical-workspace /bin/bash
goto end

:jupyter
echo Starting Jupyter analytics environment...
docker-compose up -d dskypoly-analytics
echo ✓ Jupyter started!
echo Access at: http://localhost:8888
start http://localhost:8888
goto end

:shell
echo Opening shell in DSKYpoly container...
docker exec -it dskypoly-mathematical-workspace /bin/bash
goto end

:stop
echo Stopping all DSKYpoly containers...
docker-compose down
echo ✓ Containers stopped!
goto end

:clean
echo Cleaning up DSKYpoly containers and images...
docker-compose down -v
docker rmi %DOCKER_IMAGE% 2>nul
docker system prune -f
echo ✓ Cleanup complete!
goto end

:status
echo DSKYpoly Container Status:
docker-compose ps
echo.
echo Docker Images:
docker images | findstr %PROJECT_NAME%
goto end

:logs
echo DSKYpoly Container Logs:
docker-compose logs --tail=50 -f
goto end

:help
echo Usage: %0 [command]
echo.
echo Commands:
echo   build       - Build the Docker image
echo   run         - Run the main development container
echo   jupyter     - Start Jupyter notebook server
echo   shell       - Get a shell in the running container
echo   stop        - Stop all DSKYpoly containers
echo   clean       - Remove containers and images
echo   status      - Show container status
echo   logs        - Show container logs
echo   help        - Show this help message
echo.
echo Windows 11 Docker Desktop Integration:
echo   - Containers will appear in Docker Desktop GUI
echo   - Volumes are managed automatically
echo   - Port forwarding configured for web interfaces
echo   - Jupyter will auto-open in your default browser
echo.
goto end

:end
echo.
pause
