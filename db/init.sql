create database if not exists chatapp;
use chatapp;

CREATE TABLE if not exists rooms (
  room_name VARCHAR(200),
  username VARCHAR(200),
  msg VARCHAR(200),
  msg_date VARCHAR(200)
);
