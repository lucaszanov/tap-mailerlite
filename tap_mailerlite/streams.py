"""Stream type classes for tap-mailerlite."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailerlite.client import mailerliteStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.

class SubscriberStream(mailerliteStream):
    """Define custom stream."""
    name = "subscribers"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    records_jsonpath = "$.subscribers[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType, description="The user's id"),
        th.Property(
            "name",
            th.StringType,
            description="The user's name"
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email address"
        ),
        th.Property("sent", th.IntegerType),
        th.Property("opened", th.IntegerType),
        th.Property("clicked", th.IntegerType),
        th.Property("type", th.StringType),
        th.Property("signup_ip", th.StringType),
        th.Property("signup_timestamp", th.StringType),
        th.Property("confirmation_ip", th.StringType),
        th.Property("confirmation_timestamp", th.StringType),
        th.Property("fields", th.ObjectType(
            th.Property("last_name", th.StringType),
            th.Property("company", th.StringType),
            th.Property("country", th.StringType),
            th.Property("city", th.StringType),
            th.Property("phone", th.StringType),
            th.Property("state", th.StringType),
            th.Property("z_i_p", th.StringType)
            ),
        ),
        th.Property("date_subscribe", th.StringType),
        th.Property("date_unsubscribe", th.StringType),
        th.Property("date_created", th.StringType),
        th.Property("date_updated", th.StringType),
    ).to_dict()


class SubscribersGroupsStream(mailerliteStream):
    """Define custom stream."""
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    records_jsonpath = "$.groups[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType, description="ID of the group"),
        th.Property(
            "name",
            th.StringType,
            description="Title of group"
        ),
        th.Property(
            "total",
            th.IntegerType,
            description="Total count of people in group"
        ),
        th.Property(
            "active",
            th.IntegerType,
            description="Total count of active people in group"
        ),
        th.Property(
            "unsubscribed",
            th.IntegerType,
            description="Total count of unsubscribed people in group"
        ),
        th.Property(
            "bounced",
            th.IntegerType,
            description="Total count of bounced people in group"
        ),
        th.Property(
            "unconfirmed",
            th.IntegerType,
            description="Total count of unconfirmed people in group"
        ),
        th.Property(
            "junk",
            th.IntegerType,
            description="Total count of junk people in group"
        ),
        th.Property("sent", th.IntegerType,
        description = "Total count of sent emails in a group"),
        th.Property("opened", th.IntegerType,
        description = "Total count of opens in a group"),
        th.Property("clicked", th.IntegerType,
        description = "Total count of clicks in a group"),
        th.Property("date_created", th.StringType,
        description = "Date & time when group is created"),
        th.Property("date_updated", th.StringType,
        description = "Date & time when group is updated"),
    ).to_dict()


class CampaignsStream(mailerliteStream):
    """Define custom stream."""
    name = "campaigns"
    path = "/campaigns/{status}"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    records_jsonpath = "$.{status}[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType, description="ID of a campaign"),
        th.Property(
            "name",
            th.StringType,
            description="The internal campaign name"
        ),
        th.Property(
            "total_recipients",
            th.IntegerType,
            description="Total count of receivers in campaign"
        ),
        th.Property(
            "status",
            th.StringType,
            description="Possible values: sent, draft or outbox"
        ),
        th.Property(
            "type",
            th.StringType,
            description="Possible values: regular, ab, followup os rss"
        ),
        th.Property(
            "subject",
            th.StringType,
            description="The subject of the email"
        ),
        th.Property("date_created", th.StringType,
        description = "When the campaign is created"),
        th.Property("data_send", th.StringType, description =
        "When the email was sent. If campaign type is outbox, this \
            parameter will show the scheduled date."),
        th.Property("clicked", th.ObjectType(
            th.Property("count", th.IntegerType, description =
            "Total clicks of campaign. Available only for sent \
                campaigns"),
            th.Property("rate", th.FloatType, description =
            "Click rate of campaign. Available only for sent \
                campaigns")
            ),
        ),
        th.Property("opened", th.ObjectType(
            th.Property("count", th.IntegerType, description =
            "Total opens of campaign. Available only for sent \
                campaigns"),
            th.Property("rate", th.FloatType, description =
            "Open rate of campaign. Available only for sent \
                campaigns")
            ),
        ),
    ).to_dict()
