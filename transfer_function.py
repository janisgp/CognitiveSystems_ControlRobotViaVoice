# Imported Python Transfer Function
import hbp_nrp_cle.tf_framework as nrp
from hbp_nrp_cle.robotsim.RobotInterface import Topic
import geometry_msgs.msg

#################
# create global variables position, goal_state, old_command manually and paste below code
@nrp.MapRobotSubscriber("position", Topic("/gazebo/model_states", gazebo_msgs.msg.ModelStates))
@nrp.MapVariable("goal_state", initial_value=0)
@nrp.MapVariable("old_command", initial_value=333)
#################

@nrp.MapSpikeSink("output_neuron", nrp.brain.neurons[1], nrp.leaky_integrator_alpha)
@nrp.Neuron2Robot(Topic("/husky/cmd_vel", geometry_msgs.msg.Twist))
# Example TF: get output neuron voltage and output constant on robot actuator. You could do something with the voltage here and command the robot accordingly.
def turn_around(t, output_neuron, old_command, goal_state, position):
    #log the first timestep (20ms), each couple of seconds
    # executing bash command to communicate with 
    # service from local network
    import subprocess
	import tf
	
	######################
	# Insert your local IP 
    bash = 'curl Your_local_IP:5000'
	######################
	
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    command, error = process.communicate()

    current_pose = position.value.pose[position.value.name.index("robot")] 

    # Convert quaternion to Euler angles
    (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([current_pose.orientation.x, current_pose.orientation.y, current_pose.orientation.z, current_pose.orientation.w])
    current_state = yaw
    # Log Euler angles in Radians
    if t % 1 < 0.02:
        clientLogger.info('Current state: ', (roll, pitch, yaw))
    # Initialize velocity direction vectors
    motion = geometry_msgs.msg.Vector3(0,0,0)
    angular = geometry_msgs.msg.Vector3(0,0,0)

    import math
    cos45 = math.cos(math.pi / 4)  

    clientLogger.info('Command: ', command)
	
	# Translation
    if command == "go forward":
        clientLogger.info('I am going! ', command)
        motion = geometry_msgs.msg.Vector3(1,0,0)
    elif command == "go backward":
        motion = geometry_msgs.msg.Vector3(-1,0,0)
    elif command == "stop":
        motion = geometry_msgs.msg.Vector3(0,0,0)
		
    # Rotation
    elif command == "turn right":
        clientLogger.info('Goal ', goal_state.value)
        clientLogger.info('Command ', command)
        clientLogger.info('Old command before: ', old_command.value)
        if command == old_command.value:
            pass    
        else:
            goal_state.value = int((yaw - 1.57)*1000000)
            old_command.value = command
        if abs(goal_state.value/1000000 - current_state) > 0.1:
            angular = geometry_msgs.msg.Vector3(0,0,-3)
        else:
            angular = geometry_msgs.msg.Vector3(0,0,0)
    elif command == "turn left":
        clientLogger.info('Goal ', goal_state.value)
        clientLogger.info('Command ', command)
        clientLogger.info('Old command before: ', old_command.value)
        if command == old_command.value:
            pass    
        else:
            goal_state.value = int((yaw + 1.57)*1000000)
            old_command.value = command
        if abs(goal_state.value/1000000 - current_state) > 0.1:
            angular = geometry_msgs.msg.Vector3(0,0,3)
        else:
            angular = geometry_msgs.msg.Vector3(0,0,0)
    else: 
        motion = geometry_msgs.msg.Vector3(0,0,0)
    return geometry_msgs.msg.Twist(linear=motion, angular=angular)
##
