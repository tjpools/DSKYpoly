
CC=clang
CFLAGS=-Wall -Wextra -O2
TARGETS=tic_tac_toe mandelbrot game_of_life mandelbrot_zoom rotation_matrix

.PHONY: all clean tic_tac_toe mandelbrot game_of_life mandelbrot_zoom rotation_matrix
rotation_matrix: rotation_matrix.c
	@echo "🔄 Building $@ ... (animated triangle rotation)"
	$(CC) $(CFLAGS) -o $@ $< -lm
	@echo "✅ $@ ready! Run ./$@ to see matrix-powered rotation."
mandelbrot_zoom: mandelbrot_zoom.c
	@echo "🔍 Building $@ ... (animated Mandelbrot zoom)"
	$(CC) $(CFLAGS) -o $@ $<
	@echo "✅ $@ ready! Run ./$@ to see emergence in action."

all: $(TARGETS)
	@echo "🛠️  Built all targets: $(TARGETS)"

tic_tac_toe: tic_tac_toe.c
	@echo "🕹️  Building $@ ..."
	$(CC) $(CFLAGS) -o $@ $<
	@echo "✅ $@ ready! Run ./$@ to play."

mandelbrot: mandelbrot.c
	@echo "🌈 Building $@ ..."
	$(CC) $(CFLAGS) -o $@ $<
	@echo "✅ $@ ready! Run ./$@ to view Mandelbrot set."

game_of_life: game_of_life.c
	@echo "🌱 Building $@ ..."
	$(CC) $(CFLAGS) -o $@ $<
	@echo "✅ $@ ready! Run ./$@ to watch the Game of Life."

clean:
	@echo "🧹 Cleaning up..."
	rm -f $(TARGETS)
	@echo "🗑️  Done."
