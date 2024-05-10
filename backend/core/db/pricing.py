from sqlalchemy.orm import Session, joinedload, aliased, contains_eager

from ..schemas.pricing import PriceListItem
from .models import PriceListItem, ItemWithPrice


def db_get_price_list_items(db: Session):
    item_alias = aliased(ItemWithPrice)

    items = db.query(PriceListItem). \
        outerjoin(PriceListItem.items.of_type(item_alias)). \
        options(contains_eager(PriceListItem.items, alias=item_alias)). \
        order_by(PriceListItem.id, item_alias.id). \
        all()

    return items


def db_create_price_list_item(item: PriceListItem, db: Session):
    new_item = PriceListItem(
        title=item.title,
        description=item.description,
        second_description=item.second_description

    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    for item_with_price in item.items:
        new_item_with_price = ItemWithPrice(
            name=item_with_price.name,
            price=item_with_price.price,
            PriceListItem_id=new_item.id
        )
        db.add(new_item_with_price)

    db.commit()

    return new_item


def db_delete_price_list_item(item_id: int, db: Session) -> bool:
    item = db.query(PriceListItem).filter(PriceListItem.id == item_id).first()
    if not item:
        return False

    db.query(ItemWithPrice).filter(ItemWithPrice.PriceListItem_id == item_id).delete()

    db.delete(item)
    db.commit()

    return True


def db_update_price_list_item(item_id: int, updated_item_data: PriceListItem, db: Session):
    existing_item = db.query(PriceListItem).filter(PriceListItem.id == item_id).first()
    if not existing_item:
        return

    existing_item.title = updated_item_data.title
    existing_item.description = updated_item_data.description
    existing_item.second_description = updated_item_data.second_description

    db.commit()

    db.query(ItemWithPrice).filter(ItemWithPrice.PriceListItem_id == item_id).delete()

    for item_with_price in updated_item_data.items:
        new_item_with_price = ItemWithPrice(
            name=item_with_price.name,
            price=item_with_price.price,
            PriceListItem_id=item_id
        )
        db.add(new_item_with_price)

    db.commit()

    return existing_item


def db_get_price_list_item(item_id: int, db: Session):
    item_alias = aliased(ItemWithPrice)

    item = db.query(PriceListItem). \
        outerjoin(item_alias, PriceListItem.items). \
        options(joinedload(PriceListItem.items)). \
        filter(PriceListItem.id == item_id). \
        order_by(item_alias.id). \
        first()

    if not item:
        return None

    return item
