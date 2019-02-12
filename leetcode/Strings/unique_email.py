class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for mail in emails:
            local, domain = mail.split("@")
            if "+" in local:
                local = local[:local.index("+")]

            unique_emails.add(local.replace(".", "") + "@" + domain)

        return len(unique_emails)
        
