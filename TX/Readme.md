# Steps to follow for Data Validation TX

- Upload configurations in this folder to their respective 1x (VMSC 1 and VMSC 2).
- VMSC-1 and VMSC-2 .fx generation: py generate_TXfx.py
    - VMSC-1_generated.fx generated.
    - VMSC-2_generated.fx generated.
    - NOTE: different from the RX, in this test we created two different .fx files.
- Upload the workspace TX Data Validation.json to Veronte Ops' latest version:
    - Workspaces -> Add Workspace -> Import -> Select the .json
- Save the variables displayed into the complimentary telemetry:
    - Operation Panel -> Complimentary Telemetry -> Edit Period (as we are sending a static value we don't need a low period) -> Save -> Red triangle removed from the labels and values showing
- The .fx checks and commands the following:
    - Step 1: Change phase from Initial to Standby.
    - NOTE: for the autopilot to change from Initial to Standby phase, the Navigation should start. 
			For that, GNSS2 accuracy should be low and it will be necessary an initial command of yaw. 
			For the latter: Operation Panel -> Calibrations -> Advanced Calibrations -> Calibrate Yaw -> Send (any value of initial yaw should work)
      If this last step worked, you should see that the PFD widget changed.
    - Step 2: Change phase from Standby to Maintenance Rigging
    - Step 3: Check that REU Operative Mode == 2.0
    - Step 4: Check that CAN-Bus Selected == FALSE
    - Step 5: Command Target Rigging to 15.0
    - Step 6: Check that Target Rigging == 15.0
    - Step 7: Check that CLAW Outputs == Expected values
- The .fx is generated from test_values.xlsx. If a different value for the Target Rigging or CLAW Outputs is desired, it is possible to change them there to generate the .fx.
- Open STEC, select "Debug" and add the path of one of the generated .fx paths.
    - Wait for the test to end (check the UI, and a log.dlog file should have been created).
- If all checks and commands have passed, the expected TX message values can now be compared with DataBase data.
- Repeat this last step for the other .fx file.
    - WARNING: the log.dlog will be overwritten, copy the file in other folder so when you generate the next one is not overwritten too.

Notes:
    - If setUav(VMSC-1) or setUav(VMSC-2) command fail, the next results from that command are not valid.



