# Makefile


CXX=icpc

CFLAGS =  -Ilib -O3 -std=c++11
CXXFLAGS = -Ilib -O3 -std=c++11

LDFLAGS=  -lz 
# main_Updated_CNZ:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
# main_Drug_Updated_CNZ:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
Optimise_main_Drug_Updated_CNZ:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
Optimise_main_Drug_Updated_CNZ_Rudy:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
# main_lsoda_warp:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))

# Stim_Test:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
# main:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
# main_ISO:$(patsubst %.cpp,%.o,$(wildcard lib/*.cpp))
clean:
	rm lib/*.o main


