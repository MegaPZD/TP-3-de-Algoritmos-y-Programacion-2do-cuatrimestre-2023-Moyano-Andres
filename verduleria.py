import sys
import biblioteca_gention_paramentros as bio

MINIMA_LONGITUD_ARGV = 1

if __name__ == "__main__":

    if len(sys.argv) > MINIMA_LONGITUD_ARGV:
        bio.gention_parametros_consola(sys.argv)

    