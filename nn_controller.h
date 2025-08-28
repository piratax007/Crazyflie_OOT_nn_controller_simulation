//
// Created by fausto on 2024-12-10.
//

#ifndef NN_CONTROLLER_H
#define NN_CONTROLLER_H

#include "stabilizer_types.h"
#include "nn_compute.h"
#include "controller.h"

static uint32_t counter;

void rpm2pwm(control_t_n *control_n, int *PWM_0, int *PWM_1, int *PWM_2, int *PWM_3);

struct vec quat2rpy_xyz(struct quat q_xyzw);

#endif //NN_CONTROLLER_H
