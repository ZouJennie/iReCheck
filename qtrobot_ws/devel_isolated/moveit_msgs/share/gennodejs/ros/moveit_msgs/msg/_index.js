
"use strict";

let MoveGroupFeedback = require('./MoveGroupFeedback.js');
let PickupFeedback = require('./PickupFeedback.js');
let MoveGroupGoal = require('./MoveGroupGoal.js');
let PickupGoal = require('./PickupGoal.js');
let PickupActionResult = require('./PickupActionResult.js');
let PlaceAction = require('./PlaceAction.js');
let PickupActionGoal = require('./PickupActionGoal.js');
let ExecuteTrajectoryActionFeedback = require('./ExecuteTrajectoryActionFeedback.js');
let ExecuteTrajectoryActionResult = require('./ExecuteTrajectoryActionResult.js');
let PickupAction = require('./PickupAction.js');
let MoveGroupActionFeedback = require('./MoveGroupActionFeedback.js');
let ExecuteTrajectoryAction = require('./ExecuteTrajectoryAction.js');
let ExecuteTrajectoryGoal = require('./ExecuteTrajectoryGoal.js');
let MoveGroupResult = require('./MoveGroupResult.js');
let PickupActionFeedback = require('./PickupActionFeedback.js');
let PlaceGoal = require('./PlaceGoal.js');
let MoveGroupActionResult = require('./MoveGroupActionResult.js');
let PickupResult = require('./PickupResult.js');
let MoveGroupActionGoal = require('./MoveGroupActionGoal.js');
let ExecuteTrajectoryResult = require('./ExecuteTrajectoryResult.js');
let PlaceResult = require('./PlaceResult.js');
let MoveGroupAction = require('./MoveGroupAction.js');
let PlaceFeedback = require('./PlaceFeedback.js');
let ExecuteTrajectoryActionGoal = require('./ExecuteTrajectoryActionGoal.js');
let PlaceActionResult = require('./PlaceActionResult.js');
let PlaceActionGoal = require('./PlaceActionGoal.js');
let PlaceActionFeedback = require('./PlaceActionFeedback.js');
let ExecuteTrajectoryFeedback = require('./ExecuteTrajectoryFeedback.js');
let JointLimits = require('./JointLimits.js');
let CartesianPoint = require('./CartesianPoint.js');
let JointConstraint = require('./JointConstraint.js');
let MotionPlanResponse = require('./MotionPlanResponse.js');
let RobotState = require('./RobotState.js');
let CostSource = require('./CostSource.js');
let PlanningOptions = require('./PlanningOptions.js');
let AllowedCollisionMatrix = require('./AllowedCollisionMatrix.js');
let PlanningSceneWorld = require('./PlanningSceneWorld.js');
let VisibilityConstraint = require('./VisibilityConstraint.js');
let BoundingVolume = require('./BoundingVolume.js');
let ContactInformation = require('./ContactInformation.js');
let Grasp = require('./Grasp.js');
let AllowedCollisionEntry = require('./AllowedCollisionEntry.js');
let CollisionObject = require('./CollisionObject.js');
let RobotTrajectory = require('./RobotTrajectory.js');
let CartesianTrajectory = require('./CartesianTrajectory.js');
let LinkPadding = require('./LinkPadding.js');
let OrientedBoundingBox = require('./OrientedBoundingBox.js');
let DisplayTrajectory = require('./DisplayTrajectory.js');
let MoveItErrorCodes = require('./MoveItErrorCodes.js');
let PlannerParams = require('./PlannerParams.js');
let MotionPlanRequest = require('./MotionPlanRequest.js');
let PlannerInterfaceDescription = require('./PlannerInterfaceDescription.js');
let PositionConstraint = require('./PositionConstraint.js');
let CartesianTrajectoryPoint = require('./CartesianTrajectoryPoint.js');
let PlanningSceneComponents = require('./PlanningSceneComponents.js');
let KinematicSolverInfo = require('./KinematicSolverInfo.js');
let ObjectColor = require('./ObjectColor.js');
let PlaceLocation = require('./PlaceLocation.js');
let ConstraintEvalResult = require('./ConstraintEvalResult.js');
let OrientationConstraint = require('./OrientationConstraint.js');
let TrajectoryConstraints = require('./TrajectoryConstraints.js');
let LinkScale = require('./LinkScale.js');
let MotionPlanDetailedResponse = require('./MotionPlanDetailedResponse.js');
let AttachedCollisionObject = require('./AttachedCollisionObject.js');
let GripperTranslation = require('./GripperTranslation.js');
let WorkspaceParameters = require('./WorkspaceParameters.js');
let GenericTrajectory = require('./GenericTrajectory.js');
let DisplayRobotState = require('./DisplayRobotState.js');
let Constraints = require('./Constraints.js');
let PositionIKRequest = require('./PositionIKRequest.js');
let PlanningScene = require('./PlanningScene.js');

module.exports = {
  MoveGroupFeedback: MoveGroupFeedback,
  PickupFeedback: PickupFeedback,
  MoveGroupGoal: MoveGroupGoal,
  PickupGoal: PickupGoal,
  PickupActionResult: PickupActionResult,
  PlaceAction: PlaceAction,
  PickupActionGoal: PickupActionGoal,
  ExecuteTrajectoryActionFeedback: ExecuteTrajectoryActionFeedback,
  ExecuteTrajectoryActionResult: ExecuteTrajectoryActionResult,
  PickupAction: PickupAction,
  MoveGroupActionFeedback: MoveGroupActionFeedback,
  ExecuteTrajectoryAction: ExecuteTrajectoryAction,
  ExecuteTrajectoryGoal: ExecuteTrajectoryGoal,
  MoveGroupResult: MoveGroupResult,
  PickupActionFeedback: PickupActionFeedback,
  PlaceGoal: PlaceGoal,
  MoveGroupActionResult: MoveGroupActionResult,
  PickupResult: PickupResult,
  MoveGroupActionGoal: MoveGroupActionGoal,
  ExecuteTrajectoryResult: ExecuteTrajectoryResult,
  PlaceResult: PlaceResult,
  MoveGroupAction: MoveGroupAction,
  PlaceFeedback: PlaceFeedback,
  ExecuteTrajectoryActionGoal: ExecuteTrajectoryActionGoal,
  PlaceActionResult: PlaceActionResult,
  PlaceActionGoal: PlaceActionGoal,
  PlaceActionFeedback: PlaceActionFeedback,
  ExecuteTrajectoryFeedback: ExecuteTrajectoryFeedback,
  JointLimits: JointLimits,
  CartesianPoint: CartesianPoint,
  JointConstraint: JointConstraint,
  MotionPlanResponse: MotionPlanResponse,
  RobotState: RobotState,
  CostSource: CostSource,
  PlanningOptions: PlanningOptions,
  AllowedCollisionMatrix: AllowedCollisionMatrix,
  PlanningSceneWorld: PlanningSceneWorld,
  VisibilityConstraint: VisibilityConstraint,
  BoundingVolume: BoundingVolume,
  ContactInformation: ContactInformation,
  Grasp: Grasp,
  AllowedCollisionEntry: AllowedCollisionEntry,
  CollisionObject: CollisionObject,
  RobotTrajectory: RobotTrajectory,
  CartesianTrajectory: CartesianTrajectory,
  LinkPadding: LinkPadding,
  OrientedBoundingBox: OrientedBoundingBox,
  DisplayTrajectory: DisplayTrajectory,
  MoveItErrorCodes: MoveItErrorCodes,
  PlannerParams: PlannerParams,
  MotionPlanRequest: MotionPlanRequest,
  PlannerInterfaceDescription: PlannerInterfaceDescription,
  PositionConstraint: PositionConstraint,
  CartesianTrajectoryPoint: CartesianTrajectoryPoint,
  PlanningSceneComponents: PlanningSceneComponents,
  KinematicSolverInfo: KinematicSolverInfo,
  ObjectColor: ObjectColor,
  PlaceLocation: PlaceLocation,
  ConstraintEvalResult: ConstraintEvalResult,
  OrientationConstraint: OrientationConstraint,
  TrajectoryConstraints: TrajectoryConstraints,
  LinkScale: LinkScale,
  MotionPlanDetailedResponse: MotionPlanDetailedResponse,
  AttachedCollisionObject: AttachedCollisionObject,
  GripperTranslation: GripperTranslation,
  WorkspaceParameters: WorkspaceParameters,
  GenericTrajectory: GenericTrajectory,
  DisplayRobotState: DisplayRobotState,
  Constraints: Constraints,
  PositionIKRequest: PositionIKRequest,
  PlanningScene: PlanningScene,
};
