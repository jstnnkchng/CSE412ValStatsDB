-- Database: 412ValStats

--DROP DATABASE IF EXISTS "412ValStats";

CREATE DATABASE "412ValStats"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- SCHEMA: public

-- DROP SCHEMA IF EXISTS public;

CREATE SCHEMA IF NOT EXISTS public
    AUTHORIZATION postgres;

COMMENT ON SCHEMA public
    IS 'standard public schema';

GRANT ALL ON SCHEMA public TO PUBLIC;

GRANT ALL ON SCHEMA public TO postgres;

-- Table: public.ESportPerson

--DROP TABLE IF EXISTS public.ESportPerson CASCADE;

CREATE TABLE IF NOT EXISTS public.ESportPerson
(
    uid int,
    ESPname character varying,
    age int,
    country character varying,
    job character varying,
    CONSTRAINT ESportPerson_pkey PRIMARY KEY (uid)
);

-- Table: public.Coach

--DROP TABLE IF EXISTS public.Coach CASCADE;

CREATE TABLE IF NOT EXISTS public.Coach
(
    cid int REFERENCES ESportPerson(uid) UNIQUE,
    tid int,
    CONSTRAINT Coach_pkey PRIMARY KEY (cid)
);

-- Table: public.Player

--DROP TABLE IF EXISTS public.Player CASCADE;

CREATE TABLE IF NOT EXISTS public.Player
(
    pid int REFERENCES ESportPerson(uid) UNIQUE,
    tid int,
    winnings int,
    CONSTRAINT Player_pkey PRIMARY KEY (pid)
);

-- Table: public.Agent

--DROP TABLE IF EXISTS public.Agent CASCADE;

CREATE TABLE IF NOT EXISTS public.Agent
(
	pid int,
	name character varying,
	kd decimal(5,2),
	avgscore decimal(5, 2),
	CONSTRAINT Agent_pkey PRIMARY KEY (name,pid)
);

-- Table: public.Team

--DROP TABLE IF EXISTS public.Team;

CREATE TABLE IF NOT EXISTS public.Team
(
    tid int,
    country character varying,
    tname character varying,
    winnings decimal,
    CONSTRAINT Team_pkey PRIMARY KEY (tid)
);

--ALTER TABLE public.Coach ADD CONSTRAINT Coach_fkey FOREIGN KEY (tid) references public.Team(tid);
--ALTER TABLE public.Player ADD CONSTRAINT Player_fkey FOREIGN KEY (tid) references public.Team(tid);
--ALTER TABLE public.Agent ADD CONSTRAINT Agent_fkey FOREIGN KEY (pid) references public.Player(pid);

--search for specific player
SELECT DISTINCT ESportPerson.ESPname, ESportPerson.age, ESportPerson.country, Team.tname, Player.winnings
    FROM ESportPerson, Player, Team
    WHERE ESportPerson.uid = Player.pid AND Player.tid = Team.tid
    AND ESportPerson.ESPname = 'TenZ';


--search for specific team
SELECT DISTINCT Team.tname, Team.country, Team.winnings
    FROM Team
    WHERE Team.tname = 'Sentinels';

--Search for specific person's agents
SELECT DISTINCT Agent.name, Agent.kd, Agent.avgscore
    FROM Agent, Player, ESportPerson
    WHERE Player.pid = Agent.pid
      AND Player.pid = ESportPerson.uid
      AND ESportPerson.espname = 'TenZ';

--Search list of players on a team
SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country, Player.winnings
FROM ESportPerson, Player, Team
WHERE Team.tid = Player.tid AND Player.pid = ESportPerson.uid
AND Team.tname = 'Sentinels';

--search for specific coach
SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country, Team.tname
FROM ESportPerson, Coach, Team
WHERE ESportPerson.uid = Coach.cid AND Coach.tid = Team.tid
AND ESportPerson.espname = 'd00mbr0s';

--Select list of coaches on a team
SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country
FROM ESportPerson, Coach, Team
WHERE ESportPerson.uid = Coach.cid AND Coach.tid = Team.tid
AND Team.tname = 'FNATIC';

--select specific agent
SELECT DISTINCT MAX(Agent.name) , AVG(Agent.kd), AVG(Agent.avgscore)
FROM Agent
WHERE Agent.name = 'Jett';




