import pandas as pd

# Ruta al Excel con columnas: embention_id y test_value
excel_path = "test_values.xlsx"
uav_list = ["VMSC-1", "VMSC-2"]

reu_ids = list(range(3303, 3319))
cmd_ids = list(range(3464, 3480))
post_check_ids = cmd_ids.copy()
check_final_ids = list(range(3130, 3148)) + list(range(3196, 3204))
bit_id = 1433

df = pd.read_excel(excel_path)
value_map = dict(zip(df["embention_id"], df["test_value"]))

for uav in uav_list:
    lines = []

    lines.append(f"setUav({uav})\n")
    lines.append("// Set Standby phase")
    lines.append("phaseCmd(0)")
    lines.append("// Set Maintenance Rigging phase")
    lines.append("phaseCmd(1)\n")

    lines.append("// Check that REU Operative Mode == 2.0")
    for var_id in reu_ids:
        val = value_map.get(var_id, 2.0)
        lines.append(f"check(Rvar_{var_id} == {val:.1f})")

    lines.append(f"\ncheck(! Bit_{bit_id})\n")

    for var_id in cmd_ids:
        val = value_map.get(var_id, 15.0)
        lines.append(f"cmdVar(RvarId;{var_id};{val:.1f})")

    lines.append("\nsleep(2000)\n")

    for var_id in post_check_ids:
        val = value_map.get(var_id, 15.0)
        lines.append(f"check(Rvar_{var_id} == {val:.1f})")

    lines.append("\nsleep(2000)\n")

    for var_id in check_final_ids:
        val = value_map.get(var_id, 15.0)
        lines.append(f"check(Rvar_{var_id} == {val:.1f})")

    file_name = f"{uav}_generated.fx"
    with open(file_name, "w") as f:
        f.write("\n".join(lines))

    print(f"{file_name} generated.")
