
"use strict";

let SetInt16 = require('./SetInt16.js')
let SetToolModbus = require('./SetToolModbus.js')
let TCPOffset = require('./TCPOffset.js')
let GripperState = require('./GripperState.js')
let GripperMove = require('./GripperMove.js')
let ConfigToolModbus = require('./ConfigToolModbus.js')
let GetDigitalIO = require('./GetDigitalIO.js')
let GetErr = require('./GetErr.js')
let GripperConfig = require('./GripperConfig.js')
let Move = require('./Move.js')
let GetControllerDigitalIO = require('./GetControllerDigitalIO.js')
let SetLoad = require('./SetLoad.js')
let GetAnalogIO = require('./GetAnalogIO.js')
let ClearErr = require('./ClearErr.js')
let SetAxis = require('./SetAxis.js')
let SetDigitalIO = require('./SetDigitalIO.js')

module.exports = {
  SetInt16: SetInt16,
  SetToolModbus: SetToolModbus,
  TCPOffset: TCPOffset,
  GripperState: GripperState,
  GripperMove: GripperMove,
  ConfigToolModbus: ConfigToolModbus,
  GetDigitalIO: GetDigitalIO,
  GetErr: GetErr,
  GripperConfig: GripperConfig,
  Move: Move,
  GetControllerDigitalIO: GetControllerDigitalIO,
  SetLoad: SetLoad,
  GetAnalogIO: GetAnalogIO,
  ClearErr: ClearErr,
  SetAxis: SetAxis,
  SetDigitalIO: SetDigitalIO,
};
