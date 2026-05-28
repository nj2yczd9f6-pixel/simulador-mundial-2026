class Mundial2026:
    def __init__(self):
        self.grupos = {
            "A": ["México", "Sudáfrica", "Corea del Sur", "Chequia"],
            "B": ["Canadá", "Suiza", "Catar", "Gales"]
        }
        self.tablas = {}
        for grupo, equipos in self.grupos.items():
            self.tablas[grupo] = {}
            for equipo in equipos:
                self.tablas[grupo][equipo] = {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "DG": 0, "PTS": 0}

    def registrar_resultado(self, grupo, equipo1, goles1, equipo2, goles2):
        self.tablas[grupo][equipo1]["GF"] += goles1
        self.tablas[grupo][equipo1]["GC"] += goles2
        self.tablas[grupo][equipo2]["GF"] += goles2
        self.tablas[grupo][equipo2]["GC"] += goles1
        self.tablas[grupo][equipo1]["PJ"] += 1
        self.tablas[grupo][equipo2]["PJ"] += 1

        if goles1 > goles2:
            self.tablas[grupo][equipo1]["G"] += 1; self.tablas[grupo][equipo1]["PTS"] += 3; self.tablas[grupo][equipo2]["P"] += 1
        elif goles2 > goles1:
            self.tablas[grupo][equipo2]["G"] += 1; self.tablas[grupo][equipo2]["PTS"] += 3; self.tablas[grupo][equipo1]["P"] += 1
        else:
            self.tablas[grupo][equipo1]["E"] += 1; self.tablas[grupo][equipo1]["PTS"] += 1; self.tablas[grupo][equipo2]["E"] += 1; self.tablas[grupo][equipo2]["PTS"] += 1

        self.tablas[grupo][equipo1]["DG"] = self.tablas[grupo][equipo1]["GF"] - self.tablas[grupo][equipo1]["GC"]
        self.tablas[grupo][equipo2]["DG"] = self.tablas[grupo][equipo2]["GF"] - self.tablas[grupo][equipo2]["GC"]

    def mostrar_tabla_grupo(self, grupo):
        equipos_ordenados = sorted(self.tablas[grupo].items(), key=lambda x: (x[1]["PTS"], x[1]["DG"], x[1]["GF"]), reverse=True)
        print(f"\n=== TABLA EN TIEMPO REAL: GRUPO {grupo} ===")
        print(f"{'Pos':<4}{'Equipo':<16}{'PJ':<4}{'G':<4}{'E':<4}{'P':<4}{'DG':<4}{'PTS':<4}")
        print("-" * 50)
        for index, (equipo, stats) in enumerate(equipos_ordenados, start=1):
            print(f"{index:<4}{equipo:<16}{stats['PJ']:<4}{stats['G']:<4}{stats['E']:<4}{stats['P']:<4}{stats['DG']:<4}{stats['PTS']:<4}")

# ==========================================
# SECCIÓN DE PRUEBAS
# ==========================================
fixture = Mundial2026()

# Registra aquí los partidos que quieras:
fixture.registrar_resultado("A", "México", 3, "Sudáfrica", 1)
fixture.registrar_resultado("A", "Corea del Sur", 1, "Chequia", 1)

# Muestra la tabla actualizada:
fixture.mostrar_tabla_grupo("A")
