# Variables
# SCHIFRADIR = Path to Schifra Version 0.0.1 (https://www.schifra.com/downloads.html )
# STBDIR = Path to STB Libraries (https://github.com/nothings/stb)
CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC_FILES = dwt97.c wavescribe.cpp

# Build Directories
BIN_DIR = bin
DEBUG_DIR = $(BIN_DIR)/Debug
RELEASE_DIR = $(BIN_DIR)/Release

# Targets
all: debug release

debug: $(DEBUG_DIR)
	$(CXX) $(CXXFLAGS) -g -D_DEBUG -DDEBUG -I$(SCHIFRADIR) -I$(STBDIR) $(SRC_FILES) -o $(DEBUG_DIR)/WaveScribe

release: $(RELEASE_DIR)
	$(CXX) $(CXXFLAGS) -O2 -I$(SCHIFRADIR) -I$(STBDIR) $(SRC_FILES) -o $(RELEASE_DIR)/WaveScribe

$(DEBUG_DIR):
	mkdir -p $(DEBUG_DIR)

$(RELEASE_DIR):
	mkdir -p $(RELEASE_DIR)

clean:
	rm -rf $(BIN_DIR)
