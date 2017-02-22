-- MySQL dump 10.13  Distrib 5.6.24, for osx10.10 (x86_64)
--
-- Host: localhost    Database: Resource_Site
-- ------------------------------------------------------
-- Server version	5.6.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--


/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_5c87d26f1e48e75b_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_5c87d26f1e48e75b_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_6c0f7d0439f0cc38_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--


/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_11959ddc276da68a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_72af8b96db2db56_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_72af8b96db2db56_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_26b0da67bfe9fe84_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--


/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_6c36d1634c00ce69_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_6c36d1634c00ce69_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissio_user_id_4b03aa88715ad4e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--


/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


--
-- Table structure for table `blogManagement_blog`
--

DROP TABLE IF EXISTS `blogManagement_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogManagement_blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `summary` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `userName_id` int(11) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `pub_at` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `update_at` datetime(6),
  `view_times` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blogManagement_blog_userName_id_4f75c12e33d0602a_fk_auth_user_id` (`userName_id`),
  CONSTRAINT `blogManagement_blog_userName_id_4f75c12e33d0602a_fk_auth_user_id` FOREIGN KEY (`userName_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogManagement_blog`
--

--
-- Table structure for table `blogManagement_comments`
--

DROP TABLE IF EXISTS `blogManagement_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogManagement_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text COLLATE utf8_unicode_ci,
  `created_at` datetime(6) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  `blog_id` int(11),
  PRIMARY KEY (`id`),
  KEY `blogManagement_comments_64458f32` (`blog_id`),
  KEY `blogManagement_commen_author_id_66033de0b7256192_fk_auth_user_id` (`author_id`),
  CONSTRAINT `blogManagemen_blog_id_47e840fb56be2a35_fk_blogManagement_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `blogManagement_blog` (`id`),
  CONSTRAINT `blogManagement_commen_author_id_66033de0b7256192_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogManagement_comments`
--


--
-- Table structure for table `classManagement_chapters`
--

DROP TABLE IF EXISTS `classManagement_chapters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_chapters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `intro` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classManagement_chapters_ea134da7` (`course_id`),
  CONSTRAINT `classMa_course_id_7a16f1996ef714a2_fk_classManagement_courses_id` FOREIGN KEY (`course_id`) REFERENCES `classManagement_courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_chapters`
--

--
-- Table structure for table `classManagement_courses`
--

DROP TABLE IF EXISTS `classManagement_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `intro` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6),
  `status` int(11) NOT NULL,
  `is_display` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_courses`
--



--
-- Table structure for table `classManagement_photolist`
--

DROP TABLE IF EXISTS `classManagement_photolist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_photolist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `file` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `photo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classMana_photo_id_33c02ea0f7452287_fk_classManagement_photos_id` (`photo_id`),
  CONSTRAINT `classMana_photo_id_33c02ea0f7452287_fk_classManagement_photos_id` FOREIGN KEY (`photo_id`) REFERENCES `classManagement_photos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_photolist`
--



--
-- Table structure for table `classManagement_photos`
--

DROP TABLE IF EXISTS `classManagement_photos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_photos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `intro` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `file` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `chap_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classMana_chap_id_752f254fcac0ce56_fk_classManagement_section_id` (`chap_id`),
  CONSTRAINT `classMana_chap_id_752f254fcac0ce56_fk_classManagement_section_id` FOREIGN KEY (`chap_id`) REFERENCES `classManagement_section` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_photos`
--

--
-- Table structure for table `classManagement_reply`
--

DROP TABLE IF EXISTS `classManagement_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_reply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text COLLATE utf8_unicode_ci,
  `created` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL,
  `video_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classManagement_reply_author_id_7e08b248f9eed112_fk_auth_user_id` (`author_id`),
  KEY `classManagement_reply_b58b747e` (`video_id`),
  CONSTRAINT `classManag_video_id_2da7755d2fc62820_fk_classManagement_video_id` FOREIGN KEY (`video_id`) REFERENCES `classManagement_video` (`id`),
  CONSTRAINT `classManagement_reply_author_id_7e08b248f9eed112_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_reply`
--

--
-- Table structure for table `classManagement_section`
--

DROP TABLE IF EXISTS `classManagement_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `intro` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `chap_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classMan_chap_id_2bbc625a0a63e901_fk_classManagement_chapters_id` (`chap_id`),
  CONSTRAINT `classMan_chap_id_2bbc625a0a63e901_fk_classManagement_chapters_id` FOREIGN KEY (`chap_id`) REFERENCES `classManagement_chapters` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_section`
--

--
-- Table structure for table `classManagement_video`
--

DROP TABLE IF EXISTS `classManagement_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classManagement_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `intro` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `video` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `hits` int(11) NOT NULL,
  `permission` tinyint(1) NOT NULL,
  `is_demo` tinyint(1) NOT NULL,
  `chap_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classMana_chap_id_19a34d4c8e2e588c_fk_classManagement_section_id` (`chap_id`),
  KEY `classManagement_video_user_id_2f38a7ccd3d322a6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `classMana_chap_id_19a34d4c8e2e588c_fk_classManagement_section_id` FOREIGN KEY (`chap_id`) REFERENCES `classManagement_section` (`id`),
  CONSTRAINT `classManagement_video_user_id_2f38a7ccd3d322a6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classManagement_video`
--

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_content_type_id_b73a48e797245f1_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_bb7875fe8b09444_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_bb7875fe8b09444_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_content_type_id_b73a48e797245f1_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_7e354ef23fc17cd1_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--


--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

--
-- Table structure for table `forumManagement_node`
--

DROP TABLE IF EXISTS `forumManagement_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forumManagement_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `introduction` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `topic_count` int(11) DEFAULT NULL,
  `plane_id` int(11),
  PRIMARY KEY (`id`),
  KEY `forumManagement_node_9defd8e5` (`plane_id`),
  CONSTRAINT `forumManag_plane_id_2d504778c4b971e0_fk_forumManagement_plane_id` FOREIGN KEY (`plane_id`) REFERENCES `forumManagement_plane` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forumManagement_node`
--

--
-- Table structure for table `forumManagement_plane`
--

DROP TABLE IF EXISTS `forumManagement_plane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forumManagement_plane` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forumManagement_plane`
--

--
-- Table structure for table `forumManagement_reply`
--

DROP TABLE IF EXISTS `forumManagement_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forumManagement_reply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text COLLATE utf8_unicode_ci,
  `created` datetime(6) DEFAULT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `up_vote` int(11) DEFAULT NULL,
  `down_vote` int(11) DEFAULT NULL,
  `last_touched` datetime(6) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `topic_id` int(11),
  PRIMARY KEY (`id`),
  KEY `forumManagement_reply_author_id_3bd22e385a2058f9_fk_auth_user_id` (`author_id`),
  KEY `forumManagement_reply_19b4d727` (`topic_id`),
  CONSTRAINT `forumManag_topic_id_33c777ed46d3fef6_fk_forumManagement_topic_id` FOREIGN KEY (`topic_id`) REFERENCES `forumManagement_topic` (`id`),
  CONSTRAINT `forumManagement_reply_author_id_3bd22e385a2058f9_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forumManagement_reply`
--

--
-- Table structure for table `forumManagement_topic`
--

DROP TABLE IF EXISTS `forumManagement_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forumManagement_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(160) COLLATE utf8_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8_unicode_ci,
  `hits` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `reply_count` int(11) DEFAULT NULL,
  `up_vote` int(11) DEFAULT NULL,
  `down_vote` int(11) DEFAULT NULL,
  `last_replied_time` datetime(6) DEFAULT NULL,
  `last_touched` datetime(6) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `node_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `forumManagement_topic_author_id_53a2211be83287f_fk_auth_user_id` (`author_id`),
  KEY `forumManagem_node_id_57ae96eb6c813f8d_fk_forumManagement_node_id` (`node_id`),
  CONSTRAINT `forumManagem_node_id_57ae96eb6c813f8d_fk_forumManagement_node_id` FOREIGN KEY (`node_id`) REFERENCES `forumManagement_node` (`id`),
  CONSTRAINT `forumManagement_topic_author_id_53a2211be83287f_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forumManagement_topic`
--

--
-- Table structure for table `forumManagement_vote`
--

DROP TABLE IF EXISTS `forumManagement_vote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forumManagement_vote` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) DEFAULT NULL,
  `involved_type` int(11) DEFAULT NULL,
  `occurrence_time` datetime(6) DEFAULT NULL,
  `involved_reply_id` int(11) DEFAULT NULL,
  `involved_topic_id` int(11) DEFAULT NULL,
  `involved_user_id` int(11) DEFAULT NULL,
  `trigger_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `f_involved_reply_id_1a668f308a300194_fk_forumManagement_reply_id` (`involved_reply_id`),
  KEY `fo_involved_topic_id_7799949a7ab8cdb_fk_forumManagement_topic_id` (`involved_topic_id`),
  KEY `forumManagemen_involved_user_id_17372f6a94ff9e2f_fk_auth_user_id` (`involved_user_id`),
  KEY `forumManagement_trigger_user_id_17a9127ec341e3d4_fk_auth_user_id` (`trigger_user_id`),
  CONSTRAINT `f_involved_reply_id_1a668f308a300194_fk_forumManagement_reply_id` FOREIGN KEY (`involved_reply_id`) REFERENCES `forumManagement_reply` (`id`),
  CONSTRAINT `fo_involved_topic_id_7799949a7ab8cdb_fk_forumManagement_topic_id` FOREIGN KEY (`involved_topic_id`) REFERENCES `forumManagement_topic` (`id`),
  CONSTRAINT `forumManagemen_involved_user_id_17372f6a94ff9e2f_fk_auth_user_id` FOREIGN KEY (`involved_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `forumManagement_trigger_user_id_17a9127ec341e3d4_fk_auth_user_id` FOREIGN KEY (`trigger_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forumManagement_vote`
--

--
-- Table structure for table `userManagement_normalusers`
--

DROP TABLE IF EXISTS `userManagement_normalusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userManagement_normalusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `membership` tinyint(1) NOT NULL,
  `userName` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `signature` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `userManagement_normalus_user_id_2de7d48ff2688d1a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userManagement_normalusers`
--


--
-- Table structure for table `userManagement_payment`
--

DROP TABLE IF EXISTS `userManagement_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userManagement_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `payment` decimal(10,2) NOT NULL,
  `payed_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userManagement_payment_e8701ad4` (`user_id`),
  CONSTRAINT `userManagement_payment_user_id_57c23bc00978f4c5_fk` FOREIGN KEY (`user_id`) REFERENCES `userManagement_normalusers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userManagement_payment`
--

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-06 16:47:50


