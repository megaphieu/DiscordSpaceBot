async def send_inv_all(client, source_guild_id, destination_guild_id):
    source_guild = client.get_guild(source_guild_id)
    destination_guild = client.get_guild(destination_guild_id)
    source_members = source_guild.members
    destination_members = destination_guild.members
    inv_list = await client.get_guild(destination_guild_id).invites()
    inv_url = inv_list[0].url
    member_list = [i for i in source_members if i not in destination_members]
    for member in member_list:
        if not member.bot:
            await member.send(inv_url)
