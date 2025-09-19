CC=clang
CFLAGS=-Wall -Wextra -O2
TARGET=tic_tac_toe

.PHONY: all clean

all: $(TARGET)
	@echo "🛠️  Building $(TARGET) with clang..."

$(TARGET): tic_tac_toe.c
	$(CC) $(CFLAGS) -o $(TARGET) tic_tac_toe.c
	@echo "✅ Build complete! Run ./$(TARGET) to play."

clean:
	@echo "🧹 Cleaning up..."
	rm -f $(TARGET)
	@echo "🗑️  Done."
