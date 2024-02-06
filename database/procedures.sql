-- This sql files contains a file the creates all stored procedures for Citadexx application.

-- ************************* Main Application Query Actions *******************************
-- * Get member by member ID
-- * Get member profile
-- * Get all members
-- * Get member cards
-- * Get member subscriptions
-- * Get member fines
-- * Get member account
-- * get member

-- Get members with active members
-- Active members have active subscription and are not on suspension
CREATE PROCEDURE sp_ActiveMembers ();


-- Get members without cards
CREATE PROCEDURE sp_MembersWithoutSubscription ();


-- Get suspended members
CREATE PROCEDURE sp_SuspendedMembers ();


-- Ensure all books are returned
-- Ensure all accounts have been settled
CREATE PROCEDURE sp_ClosePeriod ();

-- Get member activity report
CREATE PROCEDURE sp_GenerateMemberReport ();






-- Get all members --
CREATE PROCEDURE sp_GetMembers (
    BEGIN
        SELECT
            m.member_id,
            CONCAT_WS(" ", m.firstname, m.middlename, m.lastname) as name,

        FROM
        members as m
    END
);