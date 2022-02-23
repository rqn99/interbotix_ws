
"use strict";

let RobotInfo = require('./RobotInfo.js')
let MotorGains = require('./MotorGains.js')
let RegisterValues = require('./RegisterValues.js')
let OperatingModes = require('./OperatingModes.js')
let Reboot = require('./Reboot.js')
let TorqueEnable = require('./TorqueEnable.js')

module.exports = {
  RobotInfo: RobotInfo,
  MotorGains: MotorGains,
  RegisterValues: RegisterValues,
  OperatingModes: OperatingModes,
  Reboot: Reboot,
  TorqueEnable: TorqueEnable,
};
