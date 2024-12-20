!!!For now only works with subnets /24 and smaller.

A simple python tool, that helps with calculating your IP networks.
If you ever needed to subtract a small subnet adresses from bigger subnet, either for NAT reasons, or ACL, or anything else - you know how much time it takes to calculate all the subnets correctly.
With this tool it becomes very easy, just type in any IP in bigger subnet with mask, and then any IP in smaller subnet with mask. The result is going to be small subnets, that bigger subnet is needed to be devided to, to exclude all the addresses from the smaller subnet.

If it doesn't make sense, here is an exapmle:
  Let's say you have a subnet 192.168.0.0/25 for all office PS's. For those PCs the whole internet is visible, but Jerry takes advantage of that and spends too much time online, rather than on the company servers. 
  So you need to separate his IP's in another pool, without affecting other employees. Luckly all his devices can be viewed in subnet 192.168.0.112/31. 
  So here is what you get:
Before:
Nat pool 0 (everyone):
192.168.0.0/25

After:
NAT pool 2 (Jerry's devices):
192.168.0.112/31
NAT pool 1 (Everybody else):
192.168.0.0 /26
192.168.0.64 /27
192.168.0.96 /28
192.168.0.114 /31
192.168.0.116 /30
192.168.0.120 /29
