import pymem

dwEntityList = 0x4DFFF14
dwGlowObjectManager = 0x535A9D8
m_iGlowIndex = 0x10488
m_iTeamNum = 0xF4
dwLocalPlayer = 0xDEA964

def main():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        glow = pm.read_int(client + dwGlowObjectManager)

        if (player):
            team  = pm.read_int(player + m_iTeamNum)

            for i in range(1,32):
                entity = pm.read_int(client + dwEntityList + i *0x10)

                if (entity):
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_glow = pm.read_int(entity + m_iGlowIndex)

                    if (entity_team_id != team):
                        pm.write_float(glow + entity_glow * 0x38 + 0x8, float(0))
                        pm.write_float(glow + entity_glow * 0x38 + 0xC, float(1))
                        pm.write_float(glow + entity_glow * 0x38 + 0x10, float(0))
                        pm.write_float(glow + entity_glow * 0x38 + 0x14, float(1))
                        pm.write_int(glow + entity_glow * 0x38 + 0x28, 1)

if __name__  == '__main__':
    main()
